# -*- coding: utf-8 -*-
###############################################################################
#
#    ld Inc
#    Copyright (C) 2009-TODAY ld Inc(<http://www.ld.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields, api, _
from odoo import exceptions


class OpParent(models.Model):
    _name = "op.parent"
    _description = "Parent"

    name = fields.Many2one('res.partner', 'Name', required=True)
    user_id = fields.Many2one('res.users', string='User', store=True)
    student_ids = fields.Many2many('op.student', string='Student(s)')
    mobile = fields.Char(string='Mobile', related='name.mobile', readonly=False)
    active = fields.Boolean(default=True)
    relationship_id = fields.Many2one('op.parent.relationship',
                                      'Relation with Student', required=True)

    occupation = fields.Char(string='Occupation')
    email = fields.Char(string='Email', domain="[('communication_preference', '=', 'email')]", related='name.email')
    phone = fields.Char(string='Phone', domain="[('communication_preference', '=', 'phone')]")
    related_email = fields.Char(string='Email', compute='_compute_related_email', store=True, readonly=False)
    related_phone = fields.Char(string='Phone', compute='_compute_related_phone', store=True, readonly=False)
    communication_preference = fields.Selection([
        ('email', 'Email'),
        ('phone', 'Phone'),
    ], string='Communication Preference')
    additional_notes = fields.Text(string='Additional Notes')
    optional_relation = fields.Char(string='Optional Relation', help='Relationship with Student')
    optional_name = fields.Char(string='Optional Name')

    _sql_constraints = [(
        'unique_parent',
        'unique(name)',
        'Can not create parent multiple times.!'
    )]

    @api.depends('communication_preference')
    def _compute_related_email(self):
        for record in self:
            if record.communication_preference == 'email':
                record.related_email = record.email
            else:
                record.related_email = False

    @api.depends('communication_preference')
    def _compute_related_phone(self):
        for record in self:
            if record.communication_preference == 'phone':
                record.related_phone = record.phone
            else:
                record.related_phone = False

    @api.onchange('name')
    def _onchange_name(self):
        self.user_id = self.name.user_id and self.name.user_id.id or False

    @api.model_create_multi
    def create(self, vals_list):
        res = super(OpParent, self).create(vals_list)
        for vals in vals_list:
            if vals.get('student_ids', False) and res.name.user_id:
                student_ids = self.student_ids.browse(res.student_ids.ids)
                user_ids = [student_id.user_id.id for student_id in student_ids
                            if student_id.user_id]
                res.user_id.child_ids = [(6, 0, user_ids)]
        return res

    def write(self, vals):
        for rec in self:
            res = super(OpParent, self).write(vals)
            if vals.get('student_ids', False) and rec.name.user_id:
                student_ids = rec.student_ids.browse(rec.student_ids.ids)
                usr_ids = [student_id.user_id.id for student_id in student_ids
                           if student_id.user_id]
                rec.user_id.child_ids = [(6, 0, usr_ids)]
            rec.clear_caches()
            return res

    def unlink(self):
        for record in self:
            if record.name.user_id:
                record.user_id.child_ids = [(6, 0, [])]
            return super(OpParent, self).unlink()

    def create_parent_user(self):
        template = self.env.ref('ld_parent.parent_template_user')
        users_res = self.env['res.users']
        for record in self:
            if not record.name.email:
                raise exceptions.Warning(_('Update parent email id first.'))
            if not record.name.user_id:
                groups_id = template and template.groups_id or False
                user_ids = [
                    parent.user_id.id for
                    parent in record.student_ids if parent.user_id]
                user_id = users_res.create({
                    'name': record.name.name,
                    'partner_id': record.name.id,
                    'login': record.name.email,
                    'is_parent': True,
                    'tz': self._context.get('tz'),
                    'groups_id': groups_id,
                    'child_ids': [(6, 0, user_ids)]
                })
                record.user_id = user_id
                record.name.user_id = user_id


class OpStudent(models.Model):
    _inherit = "op.student"

    parent_ids = fields.Many2many('op.parent', string='Parent')
    parents_mail = fields.Char(string='Parents Email_ID', compute='_compute_parent_email', store=True)

    @api.depends('parent_ids')
    def _compute_parent_email(self):
        for rec in self:
            if rec.parent_ids:
                emails = [parent.email for parent in rec.parent_ids if parent.name.email]
                print('---------emails------', emails)
                rec.parents_mail = ', '.join(emails)
            else:
                rec.parents_mail = ""

    @api.model_create_multi
    def create(self, vals):
        res = super(OpStudent, self).create(vals)
        for values in vals:
            if values.get('parent_ids', False):
                for parent_id in res.parent_ids:
                    if parent_id.user_id:
                        user_ids = [student.user_id.id for student
                                    in parent_id.student_ids if student.user_id]
                        parent_id.user_id.child_ids = [(6, 0, user_ids)]
        return res

    def write(self, vals):
        res = super(OpStudent, self).write(vals)
        if vals.get('parent_ids', False):
            user_ids = []
            if self.parent_ids:
                for parent in self.parent_ids:
                    if parent.user_id:
                        user_ids = [parent.user_id.id for parent in parent.student_ids
                                    if parent.user_id]
                        parent.user_id.child_ids = [(6, 0, user_ids)]
            else:
                user_ids = self.env['res.users'].search([
                    ('child_ids', 'in', self.user_id.id)])
                for user_id in user_ids:
                    child_ids = user_id.child_ids.ids
                    child_ids.remove(self.user_id.id)
                    user_id.child_ids = [(6, 0, child_ids)]
        if vals.get('user_id', False):
            for parent_id in self.parent_ids:
                child_ids = parent_id.user_id.child_ids.ids
                child_ids.append(vals['user_id'])
                parent_id.name.user_id.child_ids = [(6, 0, child_ids)]
        self.clear_caches()
        return res

    def unlink(self):
        for record in self:
            if record.parent_ids:
                for parent_id in record.parent_ids:
                    child_ids = parent_id.user_id.child_ids.ids
                    child_ids.remove(record.user_id.id)
                    parent_id.name.user_id.child_ids = [(6, 0, child_ids)]
        return super(OpStudent, self).unlink()

    def get_parent(self):
        action = self.env.ref('ld_parent.'
                              'act_open_op_parent_view').read()[0]
        action['domain'] = [('student_ids', 'in', self.ids)]
        return action


class OpSubjectRegistration(models.Model):
    _inherit = "op.subject.registration"

    @api.model_create_multi
    def create(self, vals):
        if self.env.user.child_ids:
            raise exceptions.Warning(_('Invalid Action!\n Parent can not \
            create Subject Registration!'))
        return super(OpSubjectRegistration, self).create(vals)

    def write(self, vals):
        if self.env.user.child_ids:
            raise exceptions.Warning(_('Invalid Action!\n Parent can not edit \
            Subject Registration!'))
        return super(OpSubjectRegistration, self).write(vals)

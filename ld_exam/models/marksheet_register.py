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
from odoo.exceptions import ValidationError


class OpMarksheetRegister(models.Model):
    _name = "op.marksheet.register"
    _inherit = ["mail.thread"]
    _description = "Marksheet Register"

    exam_session_id = fields.Many2one(
        'op.exam.session', 'Exam Session',
        required=True, tracking=True)
    marksheet_line = fields.One2many(
        'op.marksheet.line', 'marksheet_reg_id', 'Marksheets')
    generated_date = fields.Date(
        'Generated Date', required=True,
        default=fields.Date.today(), tracking=True)
    generated_by = fields.Many2one(
        'res.users', 'Generated By',
        default=lambda self: self.env.uid,
        required=True, tracking=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('validated', 'Validated'),
         ('cancelled', 'Cancelled')], 'Status',
        default="draft", required=True, tracking=True)
    total_pass = fields.Integer(
        'Total Pass', compute='_compute_total_pass',
        tracking=True, store=True)
    total_failed = fields.Integer(
        'Total Fail', compute='_compute_total_failed',
        tracking=True, store=True)
    name = fields.Char('Marksheet Register', size=256, required=True,
                       tracking=True)
    result_template_id = fields.Many2one(
        'op.result.template', 'Result Template',
        required=True, tracking=True)
    active = fields.Boolean(default=True)

    @api.constrains('total_pass', 'total_failed')
    def _check_marks(self):
        for res in self:
            if (res.total_pass < 0.0) or (res.total_failed < 0.0):
                raise ValidationError(_('Enter proper pass or fail!'))

    @api.depends('marksheet_line.status')
    def _compute_total_pass(self):
        for record in self:
            count = 0
            for marksheet in record.marksheet_line:
                if marksheet.status == 'pass':
                    count += 1
            record.total_pass = count

    @api.depends('marksheet_line.status')
    def _compute_total_failed(self):
        for record in self:
            count = 0
            for marksheet in record.marksheet_line:
                if marksheet.status == 'fail':
                    count += 1
            record.total_failed = count

    def action_validate(self):
        self.state = 'validated'

        # Send result announcement emails to students
        mail_template = self.env.ref('ld_exam.email_template_result_announcement')

        for marksheet in self.marksheet_line:
            if marksheet.student_id.email:
                email_values = {
                    'email_from': self.env.user.email,
                    'email_to': marksheet.student_id.email,
                    'subject': 'Result Announcement Notification',
                    'body_html': """
                    <p>Hello {student_name},</p>
                    <p>Your result for the exam has been announced.</p>
                    <p>Exam Session: {session_name}</p>
                    <p>Announcement Date: {announcement_date}</p>
                    <p>Good luck!</p>
                    """.format(
                        student_name=marksheet.student_id.name,
                        session_name=marksheet.marksheet_reg_id.exam_session_id.name,
                        announcement_date=marksheet.generated_date,
                    ),
                    'reply_to': self.env.user.email,
                }
                # Create and send the email
                self.env['mail.mail'].create(email_values).send()

        return True

    def act_cancel(self):
        self.state = 'cancelled'

    def act_draft(self):
        self.state = 'draft'

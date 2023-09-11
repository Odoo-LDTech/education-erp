# -*- coding: utf-8 -*-
# Part of ld. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    ld Inc
#    Copyright (C) 2009-TODAY ld Inc(<http://www.ld.org>).
#
##############################################################################

from odoo import models, fields


class GradingAssigmentType(models.Model):
    _name = 'grading.assignment.type'
    _description = "Assignment Type"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    assign_type = fields.Selection([('sub', 'Subjective'),
                                    ('attendance', 'Attendance')],
                                   string='Type', default='sub')

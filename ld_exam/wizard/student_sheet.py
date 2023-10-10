from odoo import models, fields, api
import json


class StudentSheet(models.TransientModel):
    """ Student Hall Ticket Wizard """
    _name = "student.sheet"
    _description = "Student Mark-Sheet"

    exam_session_id = fields.Many2one(
        'op.exam.session', 'Exam Session', required=True,
        domain=[('state', 'not in', ['draft', 'cancel', 'schedule', 'held'])]
    )

    student_id = fields.Many2one('op.student', 'Student Name',
                                 Required=True)
    student_id_domain = fields.Char(compute="_compute_student_id_domain", readonly=True, store=False)

    @api.depends('exam_session_id')
    def _compute_student_id_domain(self):
        for rec in self:
            if rec.exam_session_id:
                student_ids = rec.exam_session_id.exam_ids.mapped('attendees_line.student_id.id')
                rec.student_id_domain = json.dumps([('id', 'in', student_ids)])
            else:
                rec.student_id_domain = False

    def print_student_sheet(self):
        data = self.read(['exam_session_id'])[0]
        return self.env.ref('ld_exam.action_student_sheet_mark').report_action(self, data=data)

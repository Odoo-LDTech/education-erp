import time
from odoo import models, api, fields


class ReportStudentSheet(models.AbstractModel):
    _name = "report.ld_exam.report_sheet"
    _description = "Exam Marksheet Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))
        docargs = {
            'doc_model': model,
            'docs': docs,
            'time': time,
        }
        return docargs

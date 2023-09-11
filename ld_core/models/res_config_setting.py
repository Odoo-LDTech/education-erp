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

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_ld_activity = fields.Boolean(string="Activity")
    module_ld_facility = fields.Boolean(string="Facility")
    module_ld_parent = fields.Boolean(string="Parent")
    module_ld_assignment = fields.Boolean(string="Assignment")
    module_ld_classroom = fields.Boolean(string="Classroom")
    module_ld_fees = fields.Boolean(string="Fees")
    module_ld_admission = fields.Boolean(string="Admission")
    module_ld_timetable = fields.Boolean(string="Timetable")
    module_ld_exam = fields.Boolean(string="Exam")
    module_ld_library = fields.Boolean(string="Library")
    module_ld_attendance = fields.Boolean(string="Attendance")
    module_ld_quiz = fields.Boolean(string="Quiz Enterprise")
    module_ld_discipline = fields.Boolean(
        string="Discipline Enterprise")
    module_ld_health_enterprise = fields.Boolean(
        string="Health Enterprise")
    module_ld_achievement_enterprise = fields.Boolean(
        string="Achievement Enterprise")
    module_ld_activity_enterprise = fields.Boolean(
        string="Activity Enterprise")
    module_ld_admission_enterprise = fields.Boolean(
        string="Admission Enterprise")
    module_ld_alumni_enterprise = fields.Boolean(
        string="Alumni Enterprise")
    module_ld_alumni_blog_enterprise = fields.Boolean(
        string="Alumni Blog Enterprise")
    module_ld_alumni_event_enterprise = fields.Boolean(
        string="Alumni Event Enterprise")
    module_ld_alumni_job_enterprise = fields.Boolean(
        string="Alumni Job Enterprise")
    module_ld_job_enterprise = fields.Boolean(
        string="Job Enterprise")
    module_ld_assignment_enterprise = fields.Boolean(
        string="Assignment Enterprise")
    module_ld_assignment_rubrics = fields.Boolean(
        string="Assignment Rubrics")
    module_ld_attendance_enterprise = fields.Boolean(
        string="Attendance Enterprise")
    module_ld_student_attendance_enterprise = fields.Boolean(
        string="Student Attendance Kiosk")
    module_ld_bigbluebutton = fields.Boolean(
        string="Bigbluebutton Enterprise")
    module_ld_campus_enterprise = fields.Boolean(
        string="Campus Enterprise")
    module_ld_classroom_enterprise = fields.Boolean(
        string="Classroom Enterprise")
    module_ld_exam_enterprise = fields.Boolean(
        string="Exam Enterprise")
    module_ld_facility_enterprise = fields.Boolean(
        string="Facility Enterprise")
    module_ld_fees_enterprise = fields.Boolean(
        string="Fees Enterprise")
    module_ld_fees_plan = fields.Boolean(
        string="Fees Plan")
    module_ld_fees_parent_bridge = fields.Boolean(
        string="Fees Parent Bridge")
    module_ld_library_barcode = fields.Boolean(
        string="Library Barcode Enterprise")
    module_ld_library_enterprise = fields.Boolean(
        string="Library Enterprise")
    module_ld_lms = fields.Boolean(
        string="LMS Enterprise")
    module_ld_lms_blog = fields.Boolean(
        string="LMS Blog Enterprise")
    module_ld_lms_forum = fields.Boolean(
        string="LMS Forum Enterprise")
    module_ld_lms_gamification = fields.Boolean(
        string="LMS Gamification Enterprise")
    module_ld_lms_sale = fields.Boolean(
        string="LMS Sale Enterprise")
    module_ld_lms_survey = fields.Boolean(
        string="LMS Survey Enterprise")
    module_ld_meeting_enterprise = fields.Boolean(
        string="Meeting Enterprise")
    module_ld_online_admission = fields.Boolean(
        string="Online Admission Enterprise")
    module_ld_parent_enterprise = fields.Boolean(
        string="Parent Enterprise")
    module_ld_placement_enterprise = fields.Boolean(
        string="Placement Enterprise")
    module_ld_placement_job_enterprise = fields.Boolean(
        string="Placement Job Enterprise")
    module_ld_scholarship_enterprise = fields.Boolean(
        string="Scholarship Enterprise")
    module_ld_timetable_enterprise = fields.Boolean(
        string="Timetable Enterprise")
    module_ld_transportation_enterprise = fields.Boolean(
        string="Transportation Enterprise")
    module_ld_lesson = fields.Boolean(
        string="Lesson Enterprise")
    module_ld_skill_enterprise = fields.Boolean(
        string="Skill Enterprise")
    module_ld_lms_website = fields.Boolean(
        string="LMS Website")
    module_ld_assignment_grading_enterprise = fields.Boolean(
        string="Assignment Grading Enterprise")
    module_ld_assignment_grading_bridge = fields.Boolean(
        string="Assignment Grading Bridge")
    module_ld_fees_on_session = fields.Boolean(
        string="Fees On Session")
    module_ld_fees_on_duration = fields.Boolean(
        string="Fees On Duration")
    module_ld_lms_admission = fields.Boolean(
        string="LMS Admission")
    module_ld_backend_theme = fields.Boolean(
        string="Backend Theme")
    module_ld_crm_enterprise = fields.Boolean(
        string="CRM Enterprise")
    module_ld_dashboard_kpi = fields.Boolean(
        string="Dashboard KPI")
    module_ld_digital_library = fields.Boolean(
        string="Digital Library")
    module_ld_event_enterprise = fields.Boolean(
        string="Event Enterprise")
    module_ld_exam_gpa_enterprise = fields.Boolean(
        string="Exam GPA Enterprise")
    module_ld_exam_grading_bridge = fields.Boolean(
        string="Exam Grading Bridge")
    module_ld_googlemeet = fields.Boolean(
        string="Google Meet")
    module_ld_grading = fields.Boolean(
        string="Grading")
    module_ld_jitsi_enterprise = fields.Boolean(
        string="Jitsi Enterprise")
    module_ld_quiz_anti_cheating = fields.Boolean(
        string="Quiz Anti Cheating")
    module_ld_skypemeet = fields.Boolean(
        string="Skype Meet")
    module_ld_student_progress_enterprise = fields.Boolean(
        string="Student Progress Enterprise")
    module_ld_subject_material_allocation = fields.Boolean(
        string="Subject Material Allocation")
    module_ld_teams = fields.Boolean(
        string="Teams")
    module_ld_zoom = fields.Boolean(
        string="Zoom")
    module_ld_student_leave_enterprise = fields.Boolean(
        string="Student Leave")
    module_ld_notice_board_enterprise = fields.Boolean(
        string="Notice Board Enterprise")
    module_ld_student_skill_assessment = fields.Boolean(
        string="Skill Assessment Enterprise")
    module_ld_lms_h5p = fields.Boolean(
        string="LMS H5P Enterprise")
    module_ld_online_appointment = fields.Boolean(
        string="Online Appointment Enterprise")
    module_ld_grievance_enterprise = fields.Boolean(
        string="Grievance")
    module_ld_secure = fields.Boolean(
        string="Secure QR")
    module_ld_mass_subject_registration = fields.Boolean(
        string="Mass Subject Registration")
    module_ld_attendance_report_xlsx = fields.Boolean(
        string="Attendance Xlsx Report")
    module_ld_asset_request_enterprise = fields.Boolean(
        string="Asset Request Enterprise")
    module_ld_lms_interactive_video = fields.Boolean(
        string="Lms Interactive Video")
    module_ld_lms_drag_into_text = fields.Boolean(
        string="Lms Drag Into Text")
    module_ld_lms_match_following = fields.Boolean(
        string="Lms Match Following")
    module_ld_lms_match_images = fields.Boolean(
        string="Lms Match Images")
    module_ld_lms_multiple_choice = fields.Boolean(
        string="Lms Multiple Choice")
    module_ld_lms_numeric = fields.Boolean(
        string="Lms Numeric")
    module_ld_lms_sort_paragraphs = fields.Boolean(
        string="Lms Sort Paragraphs")
    module_ld_quiz_drag_into_text = fields.Boolean(
        string="Quiz Drag Into Text")
    module_ld_quiz_match_following = fields.Boolean(
        string="Quiz Match Following")
    module_ld_quiz_match_images = fields.Boolean(
        string="Quiz Match Images")
    module_ld_quiz_multiple_choice = fields.Boolean(
        string="Quiz Multiple Choice")
    module_ld_quiz_numeric = fields.Boolean(
        string="Quiz Numeric")
    module_ld_quiz_sort_paragraphs = fields.Boolean(
        string="Quiz Sort Paragraphs")
    module_ld_live = fields.Boolean(
        string="Live Meeting")
    module_ld_live_assignment = fields.Boolean(
        string="Live Meeting Assignment")
    module_ld_live_attendance = fields.Boolean(
        string="Live Meeting Attendance")
    module_ld_live_attentiveness = fields.Boolean(
        string="Live Meeting Attentiveness")
    module_ld_attendance_face_recognition = fields.Boolean(
        string="Attendance Face Recognition")
    module_ld_omr = fields.Boolean(
        string="OMR")

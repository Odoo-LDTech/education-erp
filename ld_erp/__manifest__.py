# -*- coding: utf-8 -*-
##############################################################################
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
##############################################################################

{
    'name': 'LD ERP',
    'version': '16.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Students, Faculties and Education Institute',
    'complexity': "easy",
    'author': 'LDTECH',
    'website': 'http://www.ldtech.in',
    'depends': [
        'ld_admission',
        'ld_assignment',
        'ld_attendance',
        'ld_library',
        'ld_parent',
        'ld_exam',
        'web_ld',
    ],
    'images': [
        'static/description/ld_erp_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

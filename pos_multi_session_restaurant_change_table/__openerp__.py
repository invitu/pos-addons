# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2016 INVITU - www.invitu.com
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Pos Restaurant Multisession Change Table',
    'version': '1.0',
    'author': 'INVITU SARL',
    'website': 'http://www.invitu.com',
    'category': 'Custom',
    'description': '''This module allows to synchronize Table Changes in Multisession Pos Restaurant.

    ''',
    'depends': [
        'base',
        'pos_change_table',
        'pos_multi_session_restaurant',
    ],
    'init_xml': [],
    'data': [
        'views/templates.xml',
    ],
    'qweb': [
    ],
    'test': [],
    'demo_xml': [],
    'active': False,
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

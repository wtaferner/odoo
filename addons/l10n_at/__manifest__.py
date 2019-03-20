# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# © 2015 WT-IO IT GmbH <https://www.wt-io-it.at>

# List of contributors:
# Mag. Wolfgang Taferner <wolfgang.taferner@wt-io-it.at>
# Josse Colpaert <jco@odoo.com>

{
    "name": "Austrian Localization",
    "version": "2.0",
    "author": "WT-IO-IT GmbH, Wolfgang Taferner",
    "website": "https://www.wt-io-it.at",
    "category": "Localization",
    'summary': "Austrian Standardized Charts & Tax",
    "description": """""",
    "depends": [
        'account',
        'base_iban',
        'base_vat',
    ],
    "data": [
        'data/account_account_tag.xml',
        'data/account_account_template.xml',
        'data/account_chart_template.xml',
        'data/account_tax_report_data.xml',
        'data/account_tax_template.xml',
        'data/account_fiscal_position_template.xml',
        'data/account_chart_template_configure_data.xml',
    ],
}

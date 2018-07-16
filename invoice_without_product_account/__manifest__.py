# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
{
    'name': "Cuenta Contable por defecto en facturas sin productos.",
    'summary': """Carga de cuenta contable por defecto en las lineas de facturas en las que no se selecciona producto.""",
    'description': """
        - Agrega campos de cuenta contable de Ingresos y Gastos en el Partner.
        - Crea proceso automático de carga por defecto al colocar una descripción en la linea de la factura.
    """,
    'author': "Falcon Solutions SpA",
    'maintainer': 'Falcon Solutions SpA',
    'website': 'http://www.falconsolutions.cl',
    'license': 'AGPL-3',
    'category': 'Account',
    'version': '10.0.1',
    'depends': ['account'],
    'data': [
        'views/res_partner_view.xml',
    ],
    'demo': [
    ],
}

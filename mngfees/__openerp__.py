# -*- encoding: utf-8 -*-
##############################################################################

{
    "name": "Fees Management",
    "version": "1.0",
    "depends": [
        "account",
         "sale",
	"product",
    ],
    "author": "Cesar Alejandro Rodriguez, Allan Maradiaga, Honduras Open Source",
    "category": "Sale",
    "description": """
    """,
    'data': [
        "views/fees_menus.xml",
        "views/course_view.xml",
    	"views/section_view.xml",
    	"views/topic_view.xml",
        "views/partner_view.xml",
	"views/contract_view.xml",
	"views/contracto_sale_sequence.xml",
	"wizard/wizard_course_view.xml",
    ],
    #'update_xml' : [
     #       'security/groups.xml',
      #      'security/ir.model.access.csv'
    #],
    'demo': [],
    'installable': True,
}

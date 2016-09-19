# -*- encoding: utf-8 -*-
from openerp import models, fields, api 
class Partner(models.Model):
	_inherit= "res.partner"

	birthdate= fields.Date("Birthdate")
	id_type = fields.Selection( [('id','Identidad'),('pasaporte','Pasaporte'),('cresidencia','Carnet Residencia')], string="ID Type")
	instructor = fields.Boolean("Es instructor?",help="Indica check si es instructor")
	student = fields.Boolean("Es estudiante?",help="Indica check si es estudiante")
	id_number =	fields.Char(string="ID",size=20)
	
	_defaults = {
		'type_id': 'id',
		'instructor': False,
		'student': False,
	}
        


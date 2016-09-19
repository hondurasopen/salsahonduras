# -*- encoding: utf-8 -*-
from openerp import models, fields, api 
class Session(models.Model):
	_name="mngfees.session"	

	name=fields.Char("Session", required= True )
	topic_id= fields.Many2one("mngfees.topic", "Topic", required= True)
	description= fields.Text("Description and notes")
	state= fields.Selection([('draft','Borrador'),('progress','Progress'),('pending','Pendiente'),('done','Done')],string='Estado',default='draft')	
	
	


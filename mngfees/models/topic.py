# -*- encoding: utf-8 -*-
from openerp import models, fields, api 
class Topic(models.Model):
	_name = "mngfees.topic"
	_order = "order"	

	name=fields.Char("Name of Topic", required= True )
	order = fields.Integer("Order", required=True)
	code= fields.Char("Code of Topic")
	resource= fields.Text("Resource for topic")
	course_id= fields.Many2one("mngfees.course","Course")
	concept= fields.Text("Definition of the topic")	
	description= fields.Text("Description and notes")	


        


# -*- encoding: utf-8 -*-
from openerp import models, fields, api 
class Course(models.Model):
	_name="mngfees.course"	

	name=fields.Char("Course name", required= True )
	code= fields.Char("Course code", required=True)
	price= fields.Float("Course amount")
	duration= fields.Integer("Duration (months)",required=True, help="Number of weeks required to teach the course")
	description= fields.Text("Notes")
	active= fields.Boolean("Active Course", default= True)
	section_ids= fields.One2many("mngfees.sections", "course_id", "Sections")
	product_cat_id= fields.Many2one("product.category","Product Category", required= True, ondelete="cascade")
	contract_id = fields.Many2one("mngfees.contractsale","Contract id", ondelete="cascade")
		

	@api.model
	def create(self,vals):
		
		obj_product= self.env["product.product"]
		values={
			'name':vals.get("name"),
			'lst_price':vals.get("price"),
			'default_code': vals.get("code"),
			'type': 'service',
			'categ_id': vals.get("product_cat_id"),
			}
		obj_product.create(values)
		return super(Course,self).create(vals)

	#TODO: Allan Validar cada campo que se rescribira en el product.product
	@api.multi
	def write(self,vals):
		obj_product=self.env["product.product"].search([("default_code","=",vals.get("code"))])
		#TODO : Arreglar write en producto
		#values={
		#	'name':vals.get("name"),		
	        #       'lst_price':vals.get("price"),
		#	'default_code': vals.get("code"),
		#	'type': 'service',
		#	'categ_id': vals.get("product_cat_id"),
		#	}
		#obj_product.write(values)
		return super(Course,self).write(vals)




        


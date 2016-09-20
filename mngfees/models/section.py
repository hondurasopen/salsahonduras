# -*- encoding: utf-8 -*-
from openerp import models, fields, api , _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from datetime import datetime, date, time, timedelta
import calendar

class Sections(models.Model):
	_name="mngfees.sections"	

	name=fields.Char("Section", required= True )
	course_id= fields.Many2one("mngfees.course", "Course", required= True)
	start_date= fields.Date("Start Date", required=True)
	end_date= fields.Date("End Date")
	duration= fields. Float("Duration")
	description= fields.Text("Description and notes")
	state= fields.Selection([('draft','Borrador'),('progress','Progress'),('cancel','Cancelada'),('done','Done')],string='Estado',default='draft')
	description= fields.Text("Description and notes")
	#contract_id= fields.Many2one("mngfees.contractsale","Contract ID")
                 

	_defaults ={
         'start_date': fields.Date.today()
        }

	@api.onchange("course_id")
	def get_course_id(self):
		self.duration= self.course_id.duration
		




	


        


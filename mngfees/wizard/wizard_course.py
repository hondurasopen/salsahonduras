from openerp import fields, models, exceptions, api, _
import base64
import csv
import cStringIO
from openerp.exceptions import except_orm, Warning, RedirectWarning
from datetime import datetime

class Contractwizard(models.TransientModel):
	_name = "mngfees.coursewizard"
    	
	course_id=fields.Many2one("mngfees.course","Course", required=True)
	section_id = fields.Many2one("mngfees.sections","Section", required=True)
	generation_date= fields.Date("Generation Date")
	_defaults = {
		'generation_date': fields.Date.today()
	}
	@api.one
	def action_selection_section(self):
		ctx = self._context
		obj_contract= self.env["mngfees.contractsale"].browse(ctx['active_id'])
		obj_contract_line= self.env["mngfees.contractsale.line"]

		date_format = "%y/%m/%d"
		a = datetime.strptime(self.section_id.end_date, "%Y-%m-%d")
		b = datetime.strptime(self.generation_date, "%Y-%m-%d")
		delta = b - a
		print delta.days # that's it

		#delta2 = self.section_id.end_date - self.generation_date
		print "="*30
		print delta
		print "="*30


		values= {
		'contract_id':obj_contract.id,
		'course_id':self.course_id.id , 
		'section_id':self.section_id.id,
		'amount': self.course_id.price,
		'fees_quantity':self.course_id.duration,
    		'start_date':self.section_id.start_date,
    		'end_date':self.section_id.end_date
                }
		
		#line_id= obj_contract_line.create(values)
		"""print "*"*500
		print line_id
		print line_id.id
		print line_id.course_id.name
		print "-"*500"""


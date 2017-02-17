from django import forms
from .models import Order

class OrderForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = (
			'order_type', 
			'rush_status',
			'address', 
			'zip_code', 
			'cad_num', 
			'county', 
			'email', 
			'gf_number',
			'title_co',
			'preparer',
			'phone', 
			'fax', 
			'current_owner',
			'buyer',
			)
		labels = {
			'address':'Address (required)',
			'zip_code':'Zip code (required)',
			'cad_num':'CAD number:',
			'email':'Email (required)',
			'gf_number':'GF number',
			'title_co':'Title Company',
			'preparer':'Submitted by (required)',
			'current_owner':'Current owner (required)',
			}

class OrderDetailForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = (
			'completed',
			'completed_by',
			'order_type',
			'address', 
			'zip_code', 
			'cad_num', 
			'county', 
			'email', 
			'gf_number',
			'title_co',
			'preparer',
			'phone', 
			'fax', 
			'current_owner',
			'buyer',
			)
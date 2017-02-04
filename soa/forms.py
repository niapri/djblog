from django import forms
from .models import Order

class OrderForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = (
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
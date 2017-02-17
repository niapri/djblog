import uuid
from datetime import date, timedelta
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import MultipleObjectsReturned
import random, string

# Create your models here.
class Order(models.Model):
	# Automatically generated fields.
	order_id = models.CharField(default=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for a in range(0,7)), 
		editable=False, 
		max_length=10)
	order_date = models.DateTimeField(default=timezone.now, editable=False)
	due_date = models.DateField(default=date.today)

	COMPLETION_CHOICES = (
		('Not Complete', 'Not Complete'),
		('Complete - Delivery Pending', 'Complete - Delivery Pending'),
		('Delivered', 'Delivered'),
		)

	completed = models.CharField(max_length=50, 
		choices=COMPLETION_CHOICES,
		default='Not Complete')

	#Order type - selected by user.
	ORDER_TYPE_CHOICES = (
		('Sale', 'Sale'),
		('Refi', 'Refinance'),
		)
	order_type = models.CharField(
		max_length=8,
		choices=ORDER_TYPE_CHOICES,
		default='SALE',
		)

	RUSH_OPTIONS = (
		('REG', '8 business days'),
		('2BD', '2 business day rush'),
		)

	rush_status = models.CharField(
		max_length=3,
		choices=RUSH_OPTIONS,
		default='REG'
		)

	slug = models.SlugField(max_length=100, default='temp')

	# Additional user-input fields that are used to prepare and deliver the order.
	address = models.CharField(max_length=100, blank=True,
		validators=[
			RegexValidator(
				regex="^(\d+\s(\w+.? ?\d+\w+)?\w+[']?\s?\w+.?)$",
				message='''This does not appear to be a valid address. 
				To submit your order we must be provided with a complete street address. 
				If an address is not available, then please provide only the street name 
				and the legal description in the CAD Number field, and leave the address blank.''',
				),
			],)
	zip_code = models.IntegerField()
	cad_num = models.CharField(max_length=100, blank=True)
	county = models.CharField(max_length=100, blank=True)
	email = models.EmailField(max_length=254)
	gf_number = models.CharField(max_length=50, blank=True)
	title_co = models.CharField(max_length=100, blank=True)
	preparer = models.CharField(max_length=100)
	phone = models.CharField(max_length=20, blank=True)
	fax = models.CharField(max_length=20, blank=True)
	current_owner = models.CharField(max_length=100)
	buyer = models.CharField(max_length=100, blank=True)

	#In-house info used for metrics, etc.
	DIVISION_CHOICES = (
		('SATX', 'San Antonio'),
		('ATX', 'Austin'), 
		('HTX', 'Houston'), 
		('DTX', 'Dallas'), 
		('MTX', 'Midland'), 
		('LTX', 'Laredo'),
		('CCTX', 'Corpus Christi'),
		)
	division = models.CharField(max_length=4, 
		choices=DIVISION_CHOICES, 
		default='NONE')

	CLOSING_TEAM = (
		('ANON', 'No Employee Linked'),
		('JBLE', 'Jamie Bledsoe'), 
		('BWI', 'Brandy Wills'),
		('BBA', 'Brittany Backman'), 
		('MFO', 'Micaela Fouda'),
		('EGL', 'Elisha Glover'),
		('NWA', 'Natasha Wawr?'),
		)

	completed_by = models.CharField(max_length=4,
		choices=CLOSING_TEAM,
		default='ANON')


	def set_due_date(self):
		odate = date.today()
		self.due_date = date.today()
		if self.rush_status == 'REG':
			business_days = 8
		elif self.rush_status == '2BD':
			business_days = 2
		if self.order_date.weekday() >=5:
			self.due_date += timedelta(days=1)
		while business_days > 0:
			self.due_date += timedelta(days=1)
			weekday = self.due_date.weekday()
			if weekday >=5:
				self.due_date += timedelta(days=1)
			business_days -=1

	def chngProcessing(self):
		None


	def check_id_conflict(self):
		try:
			Order.objects.get(order_id=self.order_id)
		except MultipleObjectsReturned:
			self.order_id = (''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for a in range(0,7)))
			self.save()	


	def __str__(self):
		return str(self.order_id)


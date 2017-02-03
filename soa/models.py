import uuid
from datetime import date, timedelta
from django.db import models
from django.utils import timezone
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
		('Complete', 'Complete'),
		('Delivered', 'Delivered'),
		)

	completed = models.CharField(max_length=25, 
		choices=COMPLETION_CHOICES,
		default='Not Complete')

	#Order type - selected by user.
	ORDER_TYPE_CHOICES = (
		('Refi', 'Refinance'),
		('Sale', 'Sale'),
		)
	order_type = models.CharField(
		max_length=8,
		choices=ORDER_TYPE_CHOICES,
		default='SALE',
		)

	# Additional user-input fields that are used to prepare and deliver the order.
	address = models.CharField(max_length=100)
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

	def __str__(self):
		return str(self.order_id)


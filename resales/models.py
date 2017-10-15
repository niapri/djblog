import uuid, re
from datetime import date, timedelta
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import MultipleObjectsReturned, ValidationError
import random, string

# Create your models here.
class Resale(models.Model):
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
		('AZ', 'Arizona Disclosure Packet'),
		('TX', 'Texas Resale Packet'),
		('CQS', 'Condo Questionnaire (1-2 pages)'),
		('CQL', 'Conso Questionnaire (more than 2 pages)'),
		)
	order_type = models.CharField(
		max_length=8,
		choices=ORDER_TYPE_CHOICES,
		)

	RUSH_OPTIONS = (
		('REG', '8 business days'),
		('2BD', '3 business day rush'),
		('24H', '24-hour rush'),
		)

	rush_status = models.CharField(
		max_length=3,
		choices=RUSH_OPTIONS,
		default='REG'
		)

	slug = models.SlugField(max_length=100, default=str(order_id))

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
		elif self.rush_status == '3BD':
			business_days = 3
		elif self.rush_status == '24H':
			business_days = 1
		if self.order_date.weekday() >=5:
			self.due_date += timedelta(days=1)
		while business_days > 0:
			self.due_date += timedelta(days=1)
			weekday = self.due_date.weekday()
			if weekday >=5:
				self.due_date += timedelta(days=1)
			business_days -=1


	def check_id_conflict(self):
		try:
			Order.objects.get(order_id=self.order_id)
		except MultipleObjectsReturned:
			self.order_id = (''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for a in range(0,7)))
			self.save()	


	# def __str__(self):
	# 	return str(self.order_id)

import uuid
from django.db import models
from django.utils import timezone
import random, string

# Create your models here.
class Order(models.Model):
	# Automatically generated fields.
	order_id = models.CharField(default=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for a in range(0,7)), 
		editable=False, max_length=10)
	order_date = models.DateTimeField(default=timezone.now)
	due_date = models.DateTimeField(default=timezone.now)
	completed = models.CharField(max_length=25, default='n')

	#Order type - selected by user.
	ORDER_TYPE_CHOICES = (
		('REFI', 'Refinance'),
		('SALE', 'Sale'),
		)
	order_type = models.CharField(
		max_length=4,
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

	def __str__(self):
		return str(self.order_id)


import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
class Order(models.Model):
	# Automatically generated fields.
	order_id = models.UUIDField(default=uuid.uuid4, editable=False)
	order_date = models.DateTimeField(default=timezone.now)
	due_date = models.DateTimeField(default=timezone.now)
	completed = models.CharField(max_length=25, default='n')

	#Order type - selected by user.
	ORDER_TYPE_CHOICES = (
		('REFI', 'refinance'),
		('SALE', 'sale'),
		)
	order_type = models.CharField(
		max_length=4,
		choices=ORDER_TYPE_CHOICES,
		default='SALE',
		)

	# Additional user-input fields that are used to prepare and deliver the order.
	address = models.CharField(max_length=100)
	zip_code = models.IntegerField()
	cad_num = models.CharField(max_length=100)
	county = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	gf_number = models.CharField(max_length=50)
	title_co = models.CharField(max_length=100)
	preparer = models.CharField(max_length=100)
	phone = models.CharField(max_length=20)
	fax = models.CharField(max_length=20)
	current_owner = models.CharField(max_length=100)
	buyer = models.CharField(max_length=100)





	def rush(self):
		None

	def __str__(self):
		return str(self.order_id)

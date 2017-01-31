from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Order

# Create your views here.
def order_new(request):
	return render(request, 'soa/order_new.html', {})
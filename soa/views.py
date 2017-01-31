from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Order
from .forms import OrderForm

# Create your views here.
def order_new(request):
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			order = form.save()
			return HttpResponseRedirect('order_confirmation')
	else:
		form = OrderForm()
	return render(request, 'soa/order_new.html', {'form':form})

def order_confirmation(request):
	return render(request, 'soa/order_confirmation.html', {})
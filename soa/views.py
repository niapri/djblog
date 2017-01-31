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
			request.session['oid'] = str(order.order_id)
			return HttpResponseRedirect('order_confirmation')
	else:
		form = OrderForm()
	return render(request, 'soa/order_new.html', {'form':form})

def order_confirmation(request):
	if request.session.has_key('oid'):
		oid = request.session.get('oid')
		del request.session['oid']
	return render(request, 'soa/order_confirmation.html', {'oid':oid})
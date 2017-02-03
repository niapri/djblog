from datetime import date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Order
from .forms import OrderForm

# Create your views here.
def soahome(request):
	return render(request, 'soa/soahome.html', {})

def order_new(request):
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			order = form.save()
			order.set_due_date()
			order.save()
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

def check_order(request):
	if request.method == 'GET':
		search_query = request.GET.get('search_box', None)
		results = Order.objects.filter(order_id=search_query)
	return render(request, 'soa/check_order.html', {'results':results})

def delivery_queue(request):
	orders = Order.objects.filter(completed='n').order_by('due_date')
	return render(request, 'soa/delivery_queue.html', {'orders':orders})
from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from .models import Order
from .forms import OrderForm, OrderDetailForm
from django.core.mail import send_mail

# Create your views here.
def soahome(request):
	return render(request, 'soa/soahome.html', {})

def order_new(request):
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			order = form.save()
			order.set_due_date()
			order.check_id_conflict()
			slug = str(order.order_id)
			order.slug = slug
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
	order = Order.objects.get(order_id = oid)
	send_mail(
		'Order Confirmation %s: Statement of Account'%oid,
		'Thank you for placing an order for a Statement of Account. Your order ID is %s' %oid,
		'niapri@gmail.com',
		[order.email],
		fail_silently=False,
		)
	return render(request, 'soa/order_confirmation.html', {'oid':oid})

def check_order(request):
	if request.method == 'GET':
		search_query = request.GET.get('search_box', None)
		results = Order.objects.filter(order_id=search_query)
	return render(request, 'soa/check_order.html', {'results':results})

def delivery_queue(request):
	orders = Order.objects.exclude(completed="Delivered").order_by('due_date')
	return render(request, 'soa/delivery_queue.html', {'orders':orders})

def order_detail(request, slug):
	order = get_object_or_404(Order, slug=slug)
	if request.method == "POST":
		form = OrderDetailForm(request.POST, instance=order)
		if form.is_valid():
			order = form.save()
			return redirect('order_detail', slug=slug)
	else:
		form = OrderDetailForm(instance=order)
	return render(request, 'soa/order_detail.html', {'form':form, 'order':order})

def order_archive(request):
	orders = Order.objects.filter(completed="Delivered").order_by('due_date')
	return render(request, 'soa/order_archive.html', {'orders':orders})

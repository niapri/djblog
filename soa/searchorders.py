from .models import Order

def search_by_id(key):
	results = Order.objects.get(order_id=key)
	return results

def search_by_address(key):
	results = Order.objects.filter(address=key)
	return results

def search_by_gf(key):
	results = Order.objects.filter(gf_number=key)
	return results

def search_by_preparer(key):
	results = Order.objects.filter(preaprer=key)
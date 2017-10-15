from django.shortcuts import render
from . import views

# Create your views here.
def resaleshome(request):
	return render(request, 'resaleshome.html', {})


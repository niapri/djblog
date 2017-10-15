from django.shortcuts import render

# Create your views here.
def taskmanagerhome(request):
	return render(request, 'taskmanager/taskmanagerhome.html', {})


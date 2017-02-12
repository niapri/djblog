from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, ContactForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})

def projects(request):
	return render(request, 'blog/projects.html', {})

def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			lead = form.save(commit=False)
			lead.contact_date = timezone.now()
			lead.save()
			# Email site admin with contact form content
			send_mail(
			'New contact form submission',
			'''
			Name: %s
			Email Address: %s
			Message: %s
			'''%(lead.name, lead.email, lead.message),
			lead.email,
			['wills.brandy@gmail.com'],
			fail_silently=False
			 )
			return redirect('thankyou')
	else:
		form = ContactForm()
	return render(request, 'blog/contact.html', {'form':form})

def thankyou(request):
	return render(request, 'blog/thankyou.html', {})

def pdftest(request):
	# Create the HttpResponse object with the appropriate PDF headers
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="test.pdf"'
	# Create the PDF object, using the response object as its 'file'.
	p = canvas.Canvas(response)
	#Draw things on the PDF. Here's where PDF generation happens. 
	p.drawString(100,100, 'Hello World.')
	p.showPage()
	p.save()
	return response






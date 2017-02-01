from django.contrib import admin
from .models import Post
from .models import Lead

# Register your models here.
admin.site.register(Post)
admin.site.register(Lead)
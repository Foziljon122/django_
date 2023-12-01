from django.contrib import admin
from.models import Task, UserProfile
from .models import Book
# Register your models here.
admin.site.register(Task)
admin.site.register(UserProfile)
admin.site.register(Book)

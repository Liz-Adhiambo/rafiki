from django.contrib import admin

from .models import Category, Profile, User

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(User)

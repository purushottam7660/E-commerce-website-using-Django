from django.contrib import admin
from products.models import Category,Products
from accounts.models import Userdetails
from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin

# class AccountInline(admin.StackedInline):
#     model=Userdetails
#     can_delete=False
#     verbose_name_plural='Userdetails'

# class CustomizedUserAdmin(UserAdmin):
#     inlines=(AccountInline,)

# Register your models here.

admin.site.register(Products)
admin.site.register(Category)
# admin.site.unregister(User)
admin.site.register(Userdetails)
from django.contrib import admin

# Register your models here.
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    #to display fields on listings page
    list_display=('id','name','email','hire_date')
    #to display links i.e which can be clicked
    list_display_links=('id','name','email','hire_date')
    #search
    search_fields=('name',)

admin.site.register(Realtor,RealtorAdmin)
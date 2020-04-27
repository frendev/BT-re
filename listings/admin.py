from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    #to display fields on listings page
    list_display=('id','title','is_published','price','list_date','realtor')
    #to display links i.e which can be clicked
    list_display_links=('title','id')
    #to filter by some option here we are taking by realtor
    list_filter=('realtor',)
    #fields whcich can be editable
    list_editable=('is_published',)
    #search
    search_fields=('price','title','address','city','state','zipcode')
    #pagination
    list_per_page=25

admin.site.register(Listing,ListingAdmin)
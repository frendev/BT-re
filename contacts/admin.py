from django.contrib import admin

# Register your models here.

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','listing','phone','email')

    list_display_links=('id','name')

    seach_fields=('name','email','listing')

    list_per_page=25


admin.site.register(Contact,ContactAdmin)
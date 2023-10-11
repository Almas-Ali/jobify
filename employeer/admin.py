from django.contrib import admin

from employeer.models import Employeer

admin.site.site_header = "Jobify Admin"
admin.site.site_title = "Jobify Admin Portal"
admin.site.index_title = "Welcome to Jobify Portal"

@admin.register(Employeer)
class EmployeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'website', 'address')
    list_filter = ('name', 'email', 'phone', 'website', 'address')
    search_fields = ('name', 'email', 'phone', 'website', 'address')
    ordering = ['name']
from django.contrib import admin

from account.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'country')
    list_filter = ('email', 'first_name', 'last_name', 'phone', 'address', 'city', 'zip_code', 'country')
    search_fields = ('email', 'first_name', 'last_name', 'phone', 'address', 'city', 'zip_code', 'country')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = ()
    readonly_fields = ('last_login', 'date_joined')
    
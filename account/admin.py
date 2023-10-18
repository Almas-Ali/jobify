from django.contrib import admin

from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'country')
    list_filter = ('email', 'first_name', 'last_name', 'phone',
                   'address', 'city', 'zip_code', 'country')
    search_fields = ('email', 'first_name', 'last_name',
                     'phone', 'address', 'city', 'zip_code', 'country')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        # (None, {'fields': ('username', 'password')}),
        # ('Personal info', {'fields': ('email', 'first_name', 'last_name', 'phone', 'address', 'city', 'zip_code', 'country')}),
        # ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        # ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined')

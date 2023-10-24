from django.contrib import admin

from message.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'created_at')
    list_filter = ('sender', 'receiver')
    search_fields = ('sender__username', 'receiver__username', 'message')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('sender', 'receiver', 'message', 'created_at')
    fieldsets = (
        ('Message', {
            'fields': ('sender', 'receiver', 'message', 'created_at')
        }),
    )

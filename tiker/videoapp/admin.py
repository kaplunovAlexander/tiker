from django.contrib import admin
from .models import RequestLog

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'timestamp', 'remote_addr', 'query_params', 'user_agent', 'text_param')
    search_fields = ('path', 'method', 'remote_addr', 'query_params', 'user_agent', 'text_param')
    list_filter = ('method', 'timestamp', 'remote_addr')

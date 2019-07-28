from django.contrib import admin
from .models import Demand
from django import forms

class DemandAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'user', 'created_at', 
        'updated_at', 'status'
    ]
    list_filter = [
        'name', 'user', 
        'created_at', 'updated_at', 
        'status'
    ]
    
    class Media:
        css = {
            'all': 
            ('/static/admin/css/basic.css',)
        }

admin.site.register(Demand, DemandAdmin)



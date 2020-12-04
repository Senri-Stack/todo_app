from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class ItemAdmin(admin.ModelAdmin):
    pass
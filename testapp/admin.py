"""
Django admin configuration.
Register models for admin panel.
"""

from django.contrib import admin
from .models import TechStack, Project, APIToken


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    """Admin for TechStack model."""
    list_display = ['name', 'color']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin for Project model."""
    list_display = ['name', 'user', 'created_at', 'updated_at']
    search_fields = ['name', 'user__username']
    list_filter = ['created_at', 'user']
    filter_horizontal = ['tech_stack']


@admin.register(APIToken)
class APITokenAdmin(admin.ModelAdmin):
    """Admin for APIToken model."""
    list_display = ['user', 'is_active', 'created_at']
    search_fields = ['user__username']
    list_filter = ['is_active', 'created_at']
    readonly_fields = ['token', 'created_at', 'regenerated_at']

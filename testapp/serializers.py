"""
Django REST Framework serializers.
Used for converting model instances to/from JSON.
"""

from rest_framework import serializers
from .models import Project, TechStack, APIToken


class TechStackSerializer(serializers.ModelSerializer):
    """Serializer for TechStack model."""
    
    class Meta:
        model = TechStack
        fields = ['id', 'name', 'logo_url', 'color']


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project model."""
    tech_stack = TechStackSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'tech_stack',
            'github_link',
            'live_link',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class APITokenSerializer(serializers.ModelSerializer):
    """Serializer for APIToken model."""
    
    class Meta:
        model = APIToken
        fields = ['token', 'created_at', 'regenerated_at', 'is_active']
        read_only_fields = ['created_at', 'regenerated_at']

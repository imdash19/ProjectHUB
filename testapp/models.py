"""
Database models for the Portfolio Hub application.
- TechStack: Technology/Framework model
- Project: User project model with ManyToMany relationship to TechStack
- APIToken: API token for user authentication
"""

from django.db import models
from django.contrib.auth.models import User
import secrets


class TechStack(models.Model):
    """
    Technology/Framework model.
    Stores technology name, logo, and color for UI display.
    """
    name = models.CharField(max_length=100, unique=True)
    logo_url = models.URLField(max_length=500, blank=True)
    color = models.CharField(max_length=7, default='#000000')  # HEX color

    class Meta:
        ordering = ['name']
        verbose_name = 'Tech Stack'
        verbose_name_plural = 'Tech Stacks'

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Project model representing a user's project.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.ManyToManyField(TechStack, related_name='projects', blank=True)
    github_link = models.URLField(max_length=500, blank=True, null=True)
    live_link = models.URLField(max_length=500, blank=True, null=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class APIToken(models.Model):
    """
    API Token model for user authentication.
    Each user can have one API token.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='api_token')
    token = models.CharField(max_length=255, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    regenerated_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'API Token'
        verbose_name_plural = 'API Tokens'

    def __str__(self):
        return f"API Token for {self.user.username}"

    @staticmethod
    def generate_token():
        """Generate a secure random token."""
        return secrets.token_urlsafe(50)

    def regenerate(self):
        """Regenerate the token."""
        from django.utils import timezone
        self.token = self.generate_token()
        self.regenerated_at = timezone.now()
        self.save()

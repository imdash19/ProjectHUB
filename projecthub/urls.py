"""
URL configuration for projecthub.
Main project URL routing.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # App URLs
    path('', include('testapp.urls')),

    # Optional: Root redirect if homepage not defined in testapp
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
]

# Serve media + static in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
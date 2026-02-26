"""
URL configuration for testapp.
"""

from django.urls import path
from . import views

urlpatterns = [
    # ============ AUTHENTICATION ============
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ============ DASHBOARD & PROJECTS ============
    path('dashboard/', views.dashboard, name='dashboard'),
    path('project/add/', views.add_project, name='add_project'),
    path('project/<int:project_id>/edit/', views.edit_project, name='edit_project'),
    path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),

    # ============ PUBLIC REST APIs ============
    path('api/health/', views.api_health_check, name='api_health'),

    # API by User ID
    path('api/user/<int:user_id>/projects/',
         views.get_user_projects,
         name='api_user_projects'),

    # API by Username (Portfolio Style)
    path('api/projects/<str:username>/',
         views.get_public_user_projects,
         name='api_projects_by_username'),
]
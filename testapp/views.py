"""
Clean Portfolio Views (No Token Authentication)
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Project, TechStack
from .forms import CustomUserCreationForm, ProjectForm
from .serializers import ProjectSerializer


# ================= AUTHENTICATION =================

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


# ================= DASHBOARD =================

@login_required(login_url='login')
def dashboard(request):
    user = request.user
    projects = user.projects.all()

    return render(request, 'dashboard.html', {
        'projects': projects,
        'total_projects': projects.count(),
    })


@login_required(login_url='login')
def add_project(request):
    tech_stacks = TechStack.objects.all().order_by('name')

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            form.save_m2m()
            return redirect('dashboard')
    else:
        form = ProjectForm()

    return render(request, 'project_form.html', {
        'form': form,
        'tech_stacks': tech_stacks,
        'selected_tech': [],
        'action': 'Add'
    })


@login_required(login_url='login')
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    tech_stacks = TechStack.objects.all().order_by('name')

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'project_form.html', {
        'form': form,
        'project': project,
        'tech_stacks': tech_stacks,
        'selected_tech': project.tech_stack.all(),
        'action': 'Edit'
    })


@login_required(login_url='login')
@require_http_methods(["POST"])
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    project.delete()
    return redirect('dashboard')


# ================= PUBLIC APIs =================

@api_view(['GET'])
def get_user_projects(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response(
            {'error': 'User not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    projects = Project.objects.filter(user=user)
    serializer = ProjectSerializer(projects, many=True)

    return Response({
        'status': 'success',
        'user_id': user.id,
        'username': user.username,
        'total_projects': projects.count(),
        'projects': serializer.data
    })


@api_view(['GET'])
def get_public_user_projects(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(
            {'error': 'User not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    projects = Project.objects.filter(user=user)
    serializer = ProjectSerializer(projects, many=True)

    return Response({
        'status': 'success',
        'username': user.username,
        'total_projects': projects.count(),
        'projects': serializer.data
    })


@api_view(['GET'])
def api_health_check(request):
    return Response({
        'status': 'API is running',
        'version': '1.0',
        'message': 'ProjectHUB API is active'
    })
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Project, Service, Resume, Skill
from .forms import ProjectForm, ServiceForm, ResumeForm, SkillForm

# rest framework imports 
from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectSerializer


def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, 'accounts/signup.html')






def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')  # Redirect to a dashboard (we'll create later)
        else:
            messages.error(request, "Invalid username or password!")
    
    return render(request, 'accounts/login.html')


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')




def landing_page(request):
    return render(request, "accounts/landing.html")


@login_required
def dashboard(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, "accounts/panels/dashboard.html", {"projects": projects})


@login_required
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect("dashboard")
    else:
        form = ProjectForm()
    return render(request, "accounts/panels/projects/add_project.html", {"form": form})


@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)  # Fetch project by UUID
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard after editing
    else:
        form = ProjectForm(instance=project)

    return render(request, 'accounts/panels/projects/edit_project.html', {'form': form, 'project': project})



@login_required
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id, user=request.user)
    if project:
        project.delete()
    return redirect("dashboard")





# Create Service
@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user  # Set the logged-in user as the owner of the service
            service.save()
            return redirect('dashboard')  # Redirect to dashboard after creating service
    else:
        form = ServiceForm()
    return render(request, 'accounts/panels/services/service_form.html', {'form': form})

# Update Service
@login_required
def service_update(request, slug):
    service = get_object_or_404(Service, slug=slug, user=request.user)  # Ensure service belongs to the logged-in user
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'accounts/service_form.html', {'form': form})

# Delete Service
@login_required
def service_delete(request, slug):
    service = get_object_or_404(Service, slug=slug, user=request.user)  # Ensure service belongs to the logged-in user
    service.delete()
    return redirect('dashboard')

# Service Detail View
def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'accounts/panels/services/service_detail.html', {'service': service})

# Service List for Dashboard (optional)
@login_required
def service_list(request):
    services = Service.objects.filter(user=request.user)  # List all services of the logged-in user
    return render(request, 'accounts/panels/services/service_list.html', {'services': services})


@login_required
# List all resumes for the current user
def resume_list(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'accounts/panels/resume/resume_list.html', {'resumes': resumes})

# View details of a specific resume
@login_required
def resume_detail(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    return render(request, 'accounts/panels/resume/resume_detail.html', {'resume': resume})

# Create a new resume
@login_required
def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            # Assign the logged-in user to the resume
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resume_list')  # Redirect to the resume list after saving
    else:
        form = ResumeForm()
    return render(request, 'accounts/panels/resume/resume_form.html', {'form': form})

# Update an existing resume
@login_required
def resume_update(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume_list')  # Redirect to the resume list after saving
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'accounts/panels/resume/resume_form.html', {'form': form})



# List all skills for the current user
@login_required
def skill_list(request):
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'accounts/panels/skills/skill_list.html', {'skills': skills})

# Create a new skill
@login_required
def skill_create(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            # Assign the logged-in user to the skill
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('skill_list')  # Redirect to the skill list after saving
    else:
        form = SkillForm()
    return render(request, 'accounts/panels/skills/skill_form.html', {'form': form})

# Update an existing skill
@login_required
def skill_update(request, pk):
    skill = get_object_or_404(Skill, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')  # Redirect to the skill list after saving
    else:
        form = SkillForm(instance=skill)
    return render(request, 'accounts/panels/skills/skill_form.html', {'form': form})



# DRF starts here: ---
class ProjectListAPI(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensure users can only see their own projects
        return Project.objects.filter(user=self.request.user)

class ProjectDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensure users can only see their own project
        return Project.objects.filter(user=self.request.user)


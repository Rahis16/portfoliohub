from django.urls import path
from .import views
from .views import ProjectListAPI, ProjectDetailAPI, ResumeListAPI
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# In accounts/urls.py
from django.http import HttpResponse


# Schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Portfolio API",
        default_version='v1',
        description="API documentation for the Portfolio Hub",
        contact=openapi.Contact(email="contact@portfoliohub.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Use AllowAny for testing
)
def test_view(request):
    return HttpResponse("Test View works!")


urlpatterns = [
    path('', views.landing_page, name="landing"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_register, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add-project/", views.add_project, name="add_project"),
    path("delete-project/<uuid:project_id>/", views.delete_project, name="delete_project"),
    path('project/edit/<uuid:project_id>/', views.edit_project, name='edit_project'),
    path('service/create/', views.service_create, name='service_create'),
    path('service/update/<slug:slug>/', views.service_update, name='service_update'),
    path('service/delete/<slug:slug>/', views.service_delete, name='service_delete'),
    path('service/<slug:slug>/', views.service_detail, name='service_detail'),
    path('services/', views.service_list, name='service_list'),  # Optional: List all user services
    path('resumes/', views.resume_list, name='resume_list'),
    path('resume/<uuid:pk>/', views.resume_detail, name='resume_detail'),
    path('resume/create/', views.resume_create, name='resume_create'),
    path('resume/<uuid:pk>/update/', views.resume_update, name='resume_update'),
    path('skills/', views.skill_list, name='skill_list'),
    path('skill/create/', views.skill_create, name='skill_create'),
    path('skill/<uuid:pk>/update/', views.skill_update, name='skill_update'),
    
    
    path('projects/', views.view_projects, name='view_projects'),
    
    
    
    # rest frame works --- 
    path('api/projects/', ProjectListAPI.as_view(), name='api_projects'),
    path('api/projects/<uuid:pk>/', ProjectDetailAPI.as_view(), name='api_project_detail'),
    path('api/user-profile/', views.user_profile_api, name='user_profile_api'),
     path('api/resume/', ResumeListAPI.as_view(), name='get_resume'),
    
    
    path('test/', test_view),  # Test basic URL
    # documentation 
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    
]
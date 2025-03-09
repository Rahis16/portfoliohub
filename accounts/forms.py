from django import forms
from .models import Project, Service, Resume, Skill

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "image", "github_link", "live_demo"]
        
        
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'price', 'icon']

    icon = forms.CharField(
        required=False,  # Makes the field optional
        widget=forms.TextInput(attrs={
            'placeholder': 'Optional: Enter icon tag (e.g., boxicons, fontawesome)'
        })
    )
        
   


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'profile_picture', 'summary', 'skills', 'experience', 
                  'education', 'certifications', 'projects', 'resume_file']
        
        

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title', 'description', 'experience', 'icon']
        
               
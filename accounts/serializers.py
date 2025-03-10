from rest_framework import serializers
from .models import Project, UserProfile, Resume
from django.conf import settings

class ProjectSerializer(serializers.ModelSerializer):
    image_url = serializers.URLField(source='image.url', required=False)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image_url', 'github_link', 'live_demo', 'slug', 'created_at']
        
        
        
class UserProfileSerializer(serializers.ModelSerializer):
    profile_pic = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'full_name', 'post', 'bio', 'nickname', 'profile_pic', 'dob', 'slug', 'created_at']

    def get_profile_pic(self, obj):
        if obj.profile_pic:
            return settings.MEDIA_URL + str(obj.profile_pic)
        return None
    
    
    
class ResumeSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField()
    resume_file = serializers.SerializerMethodField()

    class Meta:
        model = Resume
        fields = [
            'id', 'user', 'title', 'profile_picture', 'summary', 
            'skills', 'experience', 'education', 'certifications', 
            'projects', 'contact_email', 'contact_phone', 'resume_file', 'created_at'
        ]
    
    def get_profile_picture(self, obj):
        if obj.profile_picture:
            return settings.MEDIA_URL + str(obj.profile_picture)
        return None

    def get_resume_file(self, obj):
        if obj.resume_file:
            return settings.MEDIA_URL + str(obj.resume_file)
        return None    
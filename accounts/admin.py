from django.contrib import admin
from .models import Project, Service, Resume, Skill


from django.contrib import admin
from .models import UserProfile

# Register the UserProfile model using the modern method
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'nickname', 'dob', 'created_at', 'slug')
    search_fields = ('user__username', 'full_name', 'nickname')
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('full_name',)}  # Auto-generate slug based on full_name


# Register the Project model using the decorator
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'slug')
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('created_at', 'user')
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from title

# Register the Service model using the decorator
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'price', 'created_at', 'slug')
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('created_at', 'user')
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from title




@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')




@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience', 'user')
    search_fields = ('title', 'user__username')

import uuid
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class UserProfile(models.Model):
    # UUID for unique identification
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Link to the User model (one-to-one relationship)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Full name of the user
    full_name = models.CharField(max_length=255)
    
    # Nickname of the user
    nickname = models.CharField(max_length=100, blank=True, null=True)
    
    # Profile picture of the user
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # Date of birth
    dob = models.DateField(blank=True, null=True)
    
    # Slug based on the user's full name
    slug = models.SlugField(unique=True, blank=True)
    
    # Timestamp for when the profile was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    def save(self, *args, **kwargs):
        """Override save method to automatically generate slug from full_name"""
        if not self.slug:
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return the absolute URL of the user profile"""
        return reverse('userprofile_detail', kwargs={'slug': self.slug})
    



class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="projects_images/", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
    
class Service(models.Model):
    # UUID field for unique identification
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    order = models.IntegerField(default=0)
    
    # Title of the service
    title = models.CharField(max_length=255)
    
    # Slug for the service based on the title
    slug = models.SlugField(unique=True, blank=True)
    
    # Description of the service
    description = models.TextField()
    
    # Price of the service
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    icon = models.CharField(max_length=255, blank=True, null=True)
    
    # Created date for the service
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ForeignKey to User (author/owner of the service)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Override save to automatically generate slug based on title"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Get the absolute URL for the service"""
        return reverse('service_detail', kwargs={'slug': self.slug})
    
    
    
    
class Resume(models.Model):
    # UUID for unique identification
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # ForeignKey to the user (owner of the resume)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')

    # Title of the resume
    title = models.CharField(max_length=255)

    # Profile picture (optional)
    profile_picture = models.ImageField(upload_to='resume_pictures/', blank=True, null=True)

    # Summary or objective
    summary = models.TextField()

    # List of skills (comma-separated)
    skills = models.TextField()

    # Experience - A list of jobs held
    experience = models.TextField()

    # Education - A list of institutions attended
    education = models.TextField()

    # Certifications - A list of certifications
    certifications = models.TextField()

    # Notable projects - A list of projects completed
    projects = models.TextField()

    # Actual resume file (PDF, DOCX, etc.)
    resume_file = models.FileField(upload_to='resumes/')

    # Date created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    def get_absolute_url(self):
        return reverse('resume_detail', kwargs={'pk': self.pk})

        
        
        
        
        
class Skill(models.Model):
    # UUID field for unique identification
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Title of the skill
    title = models.CharField(max_length=255)
    
    # Description of the skill
    description = models.TextField()
    
    # Experience in the skill (number of years)
    experience = models.PositiveIntegerField()
    
    # Icon representing the skill (URL to image or icon)
    icon = models.CharField(max_length=255 ,blank=True, null=True)
    
    # ForeignKey to User (author/owner of the skill)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    
    # Method to represent the skill title as a string
    def __str__(self):
        return self.title        
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Repository(models.Model):
#     name = models.CharField(max_length=100)
#     is_public = models.BooleanField(default=True)
#     creator = models.ForeignKey(User, on_delete=models.CASCADE)

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add any additional user details you want to store here

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True)

#     def __str__(self):
#         return self.user.username

# from django import forms
# from .models import UserProfile

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['bio', 'avatar']

from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
# class Profile(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     id_user = models.IntegerField()
#     bio = models.TextField(blank=True)
#     profileimg = models.ImageField(upload_to='profile_images',default='profile.webp')
#     location = models.CharField(max_length=100,blank=True)

#     def __str__(self):
#         return self.user.username

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(null=True)  # Make it nullable
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='profile.webp')
    location = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.id_user:  # Automatically set id_user if not provided
            self.id_user = self.user.id
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    followers = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
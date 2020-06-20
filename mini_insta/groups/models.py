from django.db import models
from posts.models import Post
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_group = models.CharField(unique=True, max_length=256)
    description_of_group = models.TextField(blank=True, default="This Group has not their destription yet")
    members = models.ManyToManyField(User, related_name='members', related_query_name='member', blank=True)
    posts_in_group = models.ManyToManyField(Post, blank=True)


from django.db import models
from django.contrib.auth import get_user_model
import datetime
# Create your models here.

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts_image')
    caption = models.TextField(blank=True, null=True)
    date_of_publication = models.DateTimeField(auto_now_add=True)


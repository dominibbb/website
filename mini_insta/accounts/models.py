from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
           output_size = (300, 300)
           img.thumbnail(output_size)
           img.save(self.image.path)

class EmailChangeAuth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_change')
    new_email = models.EmailField(max_length=125)

    def __str__(self):
        return f'User {self.user.username} email is {self.new_email}'

    def save_changes(self, *args, **kwargs):
        user = User.objects.get(username=self.user)
        user.email = self.new_email
    

        
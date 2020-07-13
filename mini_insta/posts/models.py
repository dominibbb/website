from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django.urls import reverse
# Create your models here.

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts_image')
    caption = models.TextField(blank=True, null=True)
    date_of_publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_of_publication']

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return 'Author of post %s' % (self.author)

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='like', on_delete=models.CASCADE)
    like_author = models.OneToOneField(User, related_name='like_author', on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_of_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_of_created']

    def __str__(self):
        return 'Comment %s by %s' % (self.body, self.comment_author)



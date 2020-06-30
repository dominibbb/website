from django.forms import ModelForm
from .models import Post, Comment

#POST FORMS.PY

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
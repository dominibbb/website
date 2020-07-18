from django.forms import ModelForm
from .models import Comment

#POST FORMS.PY

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


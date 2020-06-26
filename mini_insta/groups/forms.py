from django.forms import ModelForm
from .models import Group

#GROUPS FORMS.PY

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = [ 'name_of_group', 'description_of_group']

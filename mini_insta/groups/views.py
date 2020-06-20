from django.shortcuts import render
from .forms import GroupForm
from django.views.generic.edit import FormView

# Create your views here.

class CreateGroup(FormView):
    template_name = 'create_group.html'
    form_class = GroupForm
    success_url = 'home'


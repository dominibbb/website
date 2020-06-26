from django.shortcuts import render, redirect
from .forms import GroupForm
from .models import Group
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView, DetailView, DeleteView, UpdateView)
from django.urls import reverse_lazy, reverse

# Create your views here.

@login_required
def create_group(request):
    if request.POST:
        if 'create_group' in request.POST:
            name_of_group = request.POST.get('name_of_group')
            description_of_group = request.POST.get('description_of_group')
            admin_of_group = request.user
            

            group_object = Group.objects.create(name_of_group = name_of_group, description_of_group = description_of_group, admin_of_group = admin_of_group)
            group_object.members.add(admin_of_group)
            return redirect('home')

    context = {

    }
    return render(request, 'groups/create_group.html', context)


class GroupListView(ListView):
    model = Group

class GroupDetailView(DetailView):
    model = Group

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/confirm_delete.html'

    success_url = reverse_lazy('groups:list')

    def get_queryset(self):
        user = self.request.user
        return Group.objects.filter(admin_of_group=user)

class GroupUpdateView(UpdateView):
    model = Group
    fields = ['name_of_group', 'description_of_group']
    success_url = reverse_lazy('groups:list')
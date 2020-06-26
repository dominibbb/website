from django.shortcuts import render, redirect
from .forms import GroupForm
from .models import Group
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_group(request):
    if request.POST:
        if 'create_group' in request.POST:
            name_of_group = request.POST.get('name_of_group')
            description_of_group = request.POST.get('description_of_group')
            user = request.user
            

            group_object = Group.objects.create(name_of_group = name_of_group, description_of_group = description_of_group, user = user)
            group_object.members.add(user)
            return redirect('home')

    context = {

    }
    return render(request, 'groups/create_group.html', context)



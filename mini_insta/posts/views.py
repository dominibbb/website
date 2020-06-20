from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Post

# Create your views here.
@login_required 
def create_post(request):
    if request.POST:
        if 'create_post' in request.POST:
            caption = request.POST.get('caption')
            image = request.FILES.get('image')
            user = request.user

            Post.objects.create(author=user, caption=caption, image=image)

            return redirect('home')

    context = {

    }
    return render(request, 'posts/create_post.html', context)
Good luck 
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

@login_required
def list_view(request):
    posts = Post.objects.all()
    if not posts:
        context = {}
    else:
        context = {
            'posts':posts
        }
    
    return render(request, 'posts/list_view.html', context)

@login_required
def delete_post(request, post_pk):
    if request.user == Posts.objects.get(pk=post_pk).author:
        if request.method == 'POST':
            Posts.objects.get(pk=post_pk).delete()

    return render(request, 'post_detail')



# def create_post(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = PostForm(request.POST)
#             if form.is_valid():
#                 form.save(commit=False)
#                 form.user = request.user
#                 form.save()
#                 return HttpResponseRedirect('/about/')
#         else:
#             form = PostForm()
#     return render(request, 'posts/create_post.html', {'form':form})
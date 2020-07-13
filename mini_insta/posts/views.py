from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormMixin

from .forms import CommentForm
from .models import Post, Like

def detail_view(request, pk):
    post = Post.objects.get(pk=pk)
    image = post.image
    caption = post.caption
    author = post.author
    date = post.date_of_publication

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if 'create_comment' in request.POST:

            if comment_form.is_valid():
                comment_form = comment_form.save(commit=False)
                comment_form.comment_author = request.user
                comment_form.post = post
                comment_form.body = request.POST.get('body')
                comment_form.save()
                return redirect('posts:detail', pk=pk)
        elif 'like' in request.POST:
            try:
                if Like.objects.get(post=post, like_author=request.user) in Like.objects.all():
                    Like.objects.get(post=post, like_author=request.user).delete()
                    user_like = 'like'
                    return redirect('posts:detail', pk=pk)
                else:
                    Like.objects.create(like_author=request.user, post=post)
                    user_like = 'dislike'
                    return redirect('posts:detail', pk=pk)                                        
            except:
                Like.objects.create(like_author=request.user, post=post)
                user_like = 'dislike'
                return redirect('posts:detail', pk=pk)       

    else:
        comment_form = CommentForm()


    context = {
        'post':post, 'image':image, 'caption':caption, 'author':request.user, 'date':date,
    }

    return render(request,  'posts/detail.html',context)



@login_required 
def create_post(request):
    if request.POST:
        if 'create_post' in request.POST:
            caption = request.POST.get('caption')
            image = request.FILES.get('image')
            user = request.user

            Post.objects.create(author=user, caption=caption, image=image)

            return redirect('posts:list')

    context = {

  }
    return render(request, 'posts/create_post.html', context)


class PostListView(ListView):

    model = Post
    reverse_lazy('about')




class PostDeleteView(DeleteView):

    model = Post
    template_name = 'posts/confirm_delete.html'

    success_url = reverse_lazy('posts:list')



    def get_queryset(self):
        user = self.request.user
        return Post.objects.get(author=user)



class PostUpdateView(UpdateView):

    model = Post

    fields = ['image', 'caption']

    success_message = "Updated Successfully" 

    success_url = reverse_lazy('posts:list')
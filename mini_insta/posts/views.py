from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormMixin

from .forms import CommentForm, AddCommentForm
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

            return redirect('posts:list')

    context = {

  }
    return render(request, 'posts/create_post.html', context)


class PostListView(ListView):

    model = Post
    reverse_lazy('about')

class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm
    template_name = 'posts/post_detail.html'

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.comment_author = 
        form.post = 
        return super(PostDetailView, self).form_valid(form)



class PostDeleteView(DeleteView):

    model = Post
    template_name = 'posts/confirm_delete.html'

    success_url = reverse_lazy('posts:list')



    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)



class PostUpdateView(UpdateView):

    model = Post

    fields = ['image', 'caption']

    success_message = "Updated Successfully" 

    success_url = reverse_lazy('posts:list')


# @login_required
# def list_view(request):
#     posts = Post.objects.all()
#     if not posts:
#         context = {}
#     else:
#         context = {
#             'posts':posts
#         }
    
#     return render(request, 'posts/list_view.html', context)

# @login_required
# def detail_view(request,post_id):
#     post = Posts.objects.get(id=post_id)
#     image = post.image
#     caption = post.caption
#     author = post.author
#     date = post.date_of_publicaton

#     context = {
#         # 'image' = image, 'caption' = caption, 'author' = author, 'date' = date
#     }

#     return render(request,  'posts/post_detail.html',context)

# @login_required
# def delete_post(request, post_id):
#     if request.user == Posts.objects.get(id=post_id).author:
#         if request.method == 'POST':
#             Posts.objects.get(pk=post_pk).delete()

#     return render(request, 'post_detail')



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


def add_comment(request):

    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            form.comment_author = request.user
            form.save()
            return HttpResponseRedirect('/about/')

    else:
        form = AddCommentForm()

    return render(request, 'posts/form_comment.html', {'form':form})
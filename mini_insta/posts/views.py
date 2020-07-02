from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormMixin

from .forms import CommentForm
from .models import Post

# HELP ME WITH THIS 
# This view is working but adding comment is not working
# the form displayed but i can't create comment 
# i can only create comment in admin page

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
        self.object = form.save(commit = False)
        self.object.comment_author = self.request.user
        self.object.post = self.get_object()
        return super(PostDetailView, self).form_valid(form)




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
        return Post.objects.filter(author=user)



class PostUpdateView(UpdateView):

    model = Post

    fields = ['image', 'caption']

    success_message = "Updated Successfully" 

    success_url = reverse_lazy('posts:list')
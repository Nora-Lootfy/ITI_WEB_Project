from django.shortcuts import render
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Category
from .forms import PostForm, CategoryForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.http import Http404


# Create your views here.


# def posts_info(request):
#     return render(request, 'posts/posts_index.html')
class PostList(ListView):
    model = Post
    template_name = 'categories/posts/posts_index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'categories/posts/post_details.html'


@method_decorator(staff_member_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'categories/posts/create_post.html'
    success_url = reverse_lazy("posts-index")

    def form_valid(self, form):
        form.instance.post_user_id = self.request.user
        return super().form_valid(form)
    


@method_decorator(staff_member_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'categories/posts/create_post.html'
    
    def get_success_url(self):
        post_id = self.object.id
        return reverse_lazy('post-details', kwargs={'pk': post_id}) # requires modifications
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.post_user_id != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(PostUpdate, self).dispatch(request, *args, **kwargs)

class PostDelete(DeleteView):
    model = Post
    template_name = 'categories/posts/delete_post.html'
    success_url = reverse_lazy('posts-index')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.post_user_id != self.request.user:
            raise Http404("You are not allowed to delete this Post")
        return super(PostDelete, self).dispatch(request, *args, **kwargs)

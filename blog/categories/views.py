from django.shortcuts import render
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .forms import PostForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


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
    form_class = PostForm
    template_name = 'categories/posts/create_post.html'
    success_url = 'categories/posts/posts_index.html'


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'categories/posts.update_post.html'
    def get_success_url(self):
        post_id = self.object.id
        return reverse_lazy('post-details', kwargs={'pk': post_id})

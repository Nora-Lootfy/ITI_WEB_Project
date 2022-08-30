from django.shortcuts import render
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
# Create your views here.


# def posts_info(request):
#     return render(request, 'posts/posts_index.html')


class PostList(ListView):
    model = Post
    template_name = 'main/index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'categories/post_details.html'


class PostCreate(CreateView):
    form_class = PostForm
    template_name = 'categories/create_post.html'
    success_url = reverse_lazy('index')


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'categories/update_post.html'

    def get_success_url(self):
        post_id = self.object.id
        return reverse_lazy('post-details', kwargs={'pk': post_id})

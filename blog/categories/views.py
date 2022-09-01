from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Category, Comment
from .forms import PostForm, CategoryForm, CommentForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponseRedirect


# Create your views here.


# def posts_info(request):
#     return render(request, 'posts/posts_index.html')
# like and dislike views
def likeview(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_like'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse_lazy("posts-index"))


def unlikeview(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('unpost_like'))
    post.likes.remove(request.user)
    return HttpResponseRedirect(reverse_lazy("posts-index"))


def dislikeview(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_dislike'))
    post.dislikes.add(request.user)
    return HttpResponseRedirect(reverse_lazy("posts-index"))


def undislikeview(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('undspost_like'))
    post.dislikes.remove(request.user)
    return HttpResponseRedirect(reverse_lazy("posts-index"))


class PostList(ListView):
    model = Post
    template_name = 'categories/posts/posts_index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'categories/posts/post_details.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(
            comment_post_id=self.get_object()).order_by('-comment_time')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = CommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(comment_content=request.POST.get('comment_content'),
                                comment_user_id=self.request.user,
                                comment_post_id=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


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
        # requires modifications
        return reverse_lazy('post-details', kwargs={'pk': post_id})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.post_user_id != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(PostUpdate, self).dispatch(request, *args, **kwargs)


@method_decorator(staff_member_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post
    template_name = 'categories/posts/delete_post.html'
    
    def get_success_url(self):
        user_id = self.object.id
        # requires modifications
        return reverse_lazy('admin_panel', kwargs={'pk': user_id})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.post_user_id != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(PostDelete, self).dispatch(request, *args, **kwargs)


def get_categories(request):
    my_data = Category.objects.all()
    context = {
        'categories': my_data
    }
    return render(request, 'main/index.html', context)


def subscribe(request, pk):
    category = get_object_or_404(Category, id=request.POST.get('subscribe'))
    category.subscribe.add(request.user)
    return HttpResponseRedirect(reverse_lazy("get-catiegores"))


def ussubscribe(request, pk):
    category = get_object_or_404(Category, id=request.POST.get('unsubscribe'))
    category.subscribe.remove(request.user)
    return HttpResponseRedirect(reverse_lazy("get-catiegores"))

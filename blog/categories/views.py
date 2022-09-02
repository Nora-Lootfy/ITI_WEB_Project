from pyexpat import model
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Category, Comment, ForbiddenWord
from .forms import PostForm, CategoryForm, CommentForm, ForbiddenWordForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator

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


def home(request):
    object_list = Post.get_posts_sorted()
    paginator = Paginator(object_list, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/index.html', {
        'categories': Category.get_all_categories(),
        'page_obj': page_obj,
    })

class PostDetail(DetailView):
    model = Post
    template_name = 'categories/posts/post_details.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(
            comment_post_id=self.get_object()).order_by('-comment_time')
        data['comments'] = comments_connected
        data['forbidden_words'] = ForbiddenWord.objects.all()
        if self.request.user.is_authenticated:
            data['form'] = CommentForm(instance=self.request.user)

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
    def get_success_url(self):
        user_id = self.object.post_user_id.id
        # requires modifications
        return reverse_lazy('admin_panel', kwargs={'id': user_id})

    def form_valid(self, form):
        form.instance.post_user_id = self.request.user
        return super().form_valid(form)

@method_decorator(staff_member_required, name='dispatch') 
class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/categories/create_category.html'
    def get_success_url(self):
        user_id = self.object.category_user.id
        # requires modifications
        return reverse_lazy('admin_panel', kwargs={'id': user_id})

    def form_valid(self, form):
        form.instance.category_user = self.request.user
        return super().form_valid(form)
        
@method_decorator(staff_member_required, name='dispatch') 
class ForbiddenWordCreate(CreateView):
    model = ForbiddenWord
    form_class = ForbiddenWordForm
    template_name = 'categories/categories/create_category.html'
    def get_success_url(self):
        user_id = self.object.forbidden_user.id
        # requires modifications
        return reverse_lazy('admin_panel', kwargs={'id': user_id})
    def form_valid(self, form):
        form.instance.forbidden_user = self.request.user
        return super().form_valid(form)

@method_decorator(staff_member_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'categories/posts/create_post.html'

    def get_success_url(self):
        user_id = self.object.post_user_id.id
        # requires modifications
        return reverse_lazy('admin_panel', kwargs={'id': user_id})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.post_user_id != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(PostUpdate, self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required, name='dispatch') 
class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/categories/create_category.html'
    
    def get_success_url(self):
        user_id = self.object.category_user.id
        # requires modifications
        return reverse_lazy('admin_panel', kwargs={'id': user_id})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.category_user != self.request.user:
            raise Http404("You are not allowed to edit this category")
        return super(CategoryUpdate, self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required, name='dispatch') 
class ForbiddenWordUpdate(UpdateView):
    model = ForbiddenWord
    form_class = ForbiddenWordForm
    template_name = 'categories/categories/create_category.html'
    
    def get_success_url(self):
        user_id = self.object.forbidden_user.id
        # requires modifications
        return reverse_lazy('admin_panel', kwargs={'id': user_id})

@method_decorator(staff_member_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post
    template_name = 'categories/posts/delete_post.html'
    
    def get_success_url(self):
        user_id = self.object.post_user_id.id
        # requires modifications
        return reverse_lazy('admin_panel', kwargs={'id': user_id})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.post_user_id != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(PostDelete, self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required, name='dispatch')
class CategoryDelete(DeleteView):
    model = Category
    template_name = 'categories/posts/delete_post.html'
    
    def get_success_url(self):
        user_id = self.object.category_user.id
        # requires modifications
        return reverse_lazy('admin_panel', kwargs={'id': user_id})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.category_user != self.request.user:
            raise Http404("You are not allowed to edit this category")
        return super(CategoryDelete, self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required, name='dispatch')
class ForbiddenWordDelete(DeleteView):
    model = ForbiddenWord
    template_name = 'categories/posts/delete_post.html'
    
    def get_success_url(self):
        user_id = self.object.forbidden_user.id
        # requires modifications
        return reverse_lazy('admin_panel', kwargs={'id': user_id})


def subscribe(request, pk):
    category = get_object_or_404(Category, id=request.POST.get('subscribe'))
    category.subscribe.add(request.user)
    return HttpResponseRedirect(reverse_lazy("home"))


def ussubscribe(request, pk):
    category = get_object_or_404(Category, id=request.POST.get('unsubscribe'))
    category.subscribe.remove(request.user)
    return HttpResponseRedirect(reverse_lazy("home"))

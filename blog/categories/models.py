from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.shortcuts import reverse

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=20, verbose_name='name')
    category_description = models.CharField(
        max_length=100, verbose_name='description')
    category_user = models.ManyToManyField(
        User, null=True, related_name='cat_user', verbose_name='user')
    subscribe = models.ManyToManyField(
        User, related_name='subscribe', blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'categories'

    @classmethod
    def get_all_categories(cls):
        return Category.objects.all()

    def totalsubscribs(self):
        return self.subscribe.count()

class Post(models.Model):
    post_title = models.CharField(
        max_length=20, null=False, verbose_name='title')
    post_image = models.ImageField(
        upload_to='categories/post/images/', null=True, verbose_name='image')
    post_content = models.TextField(null=True)
    post_category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, verbose_name='category')
    tags = TaggableManager()
    post_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name='user')
    post_created_at = models.DateTimeField(auto_now_add=True, null=True)
    post_updated_at = models.DateTimeField(auto_now=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes = models.ManyToManyField(
        User, related_name='dislikes', blank=True)

    def __str__(self):
        return self.post_title

    @classmethod
    def get_all_posts(cls):
        return Post.objects.all()

    def get_image_url(self):
        return f"/media/{self.post_image}"

    def get_post_url(self):
        return reverse("edit-post", args=[self.id])

    def total_likes(self):
        return self.likes.count()

    def total_dis_likes(self):
        return self.dislikes.count()

    @property
    def number_of_comments(self):
        return Comment.objects.filter(comment_post_id=self).count()


class Comment(models.Model):
    comment_content = models.TextField(max_length=200)
    comment_post_id = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    comment_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['comment_time']

    def __str__(self):
        return '{} commented on {}.'. format(self.comment_user_id, self.comment_post_id.post_title)


class ForbiddenWord(models.Model):
    forbidden_word = models.CharField(max_length=200)

    @classmethod
    def get_all_forbidden_words(cls):
        return cls.objects.all()

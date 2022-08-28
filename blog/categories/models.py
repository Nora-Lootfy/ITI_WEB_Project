from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=20, verbose_name='name')
    category_description = models.CharField(max_length=100, verbose_name='description')
    category_image = models.ImageField(upload_to='posts/images', null=True, verbose_name='image')
    category_user = models.ManyToManyField(User, null=True, related_name='cat_user', verbose_name='user')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'categories'


class Tag(models.Model):
    tag_name = models.CharField(max_length=20, null=False, unique=True)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    post_title = models.CharField(max_length=20, null=False, verbose_name='title')
    post_image = models.ImageField(upload_to='posts/images', null=True, verbose_name='image')
    post_content = models.TextField(null=True)
    post_category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, verbose_name='category')
    post_tags = models.ManyToManyField(Tag, null=True, blank=True, verbose_name='tags')
    post_user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='user')
    post_created_at = models.DateTimeField(auto_now_add=True, null=True)
    post_updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    comment_content = models.TextField(max_length=200)
    comment_post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} commented on {}.'. format(self.comment_user_id, self.comment_post_id.post_title)




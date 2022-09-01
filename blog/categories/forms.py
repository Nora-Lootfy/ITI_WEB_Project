from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Post, Category, Comment, ForbiddenWord

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title', 'post_content', 'post_image', 'tags', 'post_category_id', )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'category_description')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)

class ForbiddenWordForm(forms.ModelForm):
    class Meta:
        model = ForbiddenWord
        fields = ("forbidden_word", )

from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']  # Fields to include in the form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # Fields to include in the form

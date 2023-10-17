from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'created_at')
    list_filter = ('author', 'pub_date')
    search_fields = ('title', 'text')
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date')
    list_filter = ('post', 'author', 'created_date')
    search_fields = ('author', 'text')
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)

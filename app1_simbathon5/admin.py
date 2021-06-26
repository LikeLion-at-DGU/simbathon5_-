from django.contrib import admin
from .models import Comment, FAQ, Post

# Register your models here.

admin.site.register(FAQ)
admin.site.register(Post)
admin.site.register(Comment)
from django.shortcuts import render
from app1_simbathon5.models import Post
from django.contrib.auth.models import User
# Create your views here.

def mypage(request):
    user = request.user
    posts = Post.objects.filter(writer = user)
    return render(request, 'users/mypage.html', {'posts':posts})
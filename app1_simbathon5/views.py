from django.db.models.query_utils import Q
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import FAQ
from .models import QNA
# Create your views here.

def showmain(request):
    return render(request, 'app1_simbathon5/main.html')

def frequentlyaskedquestions(request):
    faqs = FAQ.objects.all()
    return render(request, 'app1_simbathon5/FAQ.html',{'faqs':faqs})

def detail(request, id):
    faq = get_object_or_404 (FAQ, pk = id)
    return render(request, 'app1_simbathon5/detail.html',{'faq':faq})

def qna (request):
    qnas = QNA.objects.all()
    return render(request, 'app1_simbathon5/Q&A.html',{'qnas':qnas})

def detail(request, id):
    faq = get_object_or_404 (QNA, pk = id)
    return render(request, 'app1_simbathon5/detail.html',{'qna':qna})


def book(request):
    return render(request, 'app1_simbathon5/book.html')
    
def main(request):
    return render(request, 'app1_simbathon5/main.html')

def newcopy(request):
    return render(request, 'app1_simbathon5/newcopy.html')

def new(request):
    return render(request, 'app1_simbathon5/new.html')


def create(request):
    new_post = FAQ()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('detail',new_post.id)

def edit(request, id):
    edit_post = FAQ.objects.get(id=id)
    return render(request, 'app1_simbathon5/edit.html' , {'post' : edit_post})

def update(request, id):
    update_post = FAQ.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer =request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('detail', update_post.id)

def delete(request, id):
    delete_post = FAQ.objects.get(id=id)
    delete_post.delete()
    return redirect('frequentlyaskedquestions')

def create(request):
    new_post = QNA()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('detail',new_post.id)

def edit(request, id):
    edit_post = QNA.objects.get(id=id)
    return render(request, 'app1_simbathon5/edit.html' , {'post' : edit_post})

def update(request, id):
    update_post = QNA.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer =request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('detail', update_post.id)

def delete(request, id):
    delete_post = QNA.objects.get(id=id)
    delete_post.delete()
    return redirect('qna')
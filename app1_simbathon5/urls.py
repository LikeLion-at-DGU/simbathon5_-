from typing import NewType
from django.urls import path,include
from .views import *
from app1_simbathon5 import views
app_name = "app1_simbathon5"
urlpatterns = [
    path('', main, name= "main"),
    path('FAQ/', frequentlyaskedquestions , name= "frequentlyaskedquestions"),
    path('QNA/', qna , name= "qna"),
    path('<str:id>', detail, name="detail"),
    path('newcopy/',newcopy, name="newcopy"),
    path('new/', new, name="new"),
    path('create/',create, name="create"),
    path('edit/<str:id>',edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
    path('book/', book,name="book"),
    path('showmain/',showmain,name="showmain"),
]
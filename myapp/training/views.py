from django.shortcuts import render
from .models import Unnes

from .forms import UnnesForm

# Create your views here.

def show_unnes_form(request, *args, **kwargs):
    form = UnnesForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form' : form
    }
    return render(request,"checkmyform.html", context )

def short(request, *args, **kwargs): #request = просто url строка
    dict ={
        "allthedata" : Unnes.objects.all(),
        "obj" : Unnes.objects.get(id=1),
    }
    return render(request, 'base.html', dict )

def secondview(request, *args, **kwargs):
    diction = {
        "positive_answer" : "Of course, I've always wanted to visit that place!",
        "one" : "two",
        "two" : "three",
        }
    return render(request, 'two_words.html', diction)

def extend(request, *args, **kwargs):
    return render(request, 'additionalhtml.html')

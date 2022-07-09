from django.shortcuts import render
from .models import Parametr

# Create your views here.

def show_homepage(request, *args, **kwargs):

    data = request.POST
    val = 15
    context = {
        "data" : data,
        "data1": val,
    }
    return render(request, "homepage.html", context)


def show_ext(request, *args, **kwargs):

    form = 15
    context = {
        'form' : form,    #передаем объект, который потом и используется в html как form.as_p
    }
    return render(request,"ext_home.html", context)

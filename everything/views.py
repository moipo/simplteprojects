from django.shortcuts import render

# Create your views here.

def show_homepage(request, *args, **kwargs):     
    return render(request, "homepage.html", {})

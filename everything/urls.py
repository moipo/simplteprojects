from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_homepage ),
    path('', views.show_ext),

]

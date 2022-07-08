from django.urls import path #для использования urlpatters, в которой ищет django
from . import views #чтобы мочь связывать url с нашими представлениями приложения

urlpatterns = [
    path('', views.show_form, name = "s") ,
    path('showten', views.showten, name = "show") ,
]

'''
path() be like: если клиент переходит по ссылке с
 названием "имя домена " + "ничего", то мы перенаправляем его на представление "short"
 в html (или в Django, я не знаю) будет это представление называться short
'''

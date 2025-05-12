# myproject/urls.py

from django.contrib import admin
from django.urls import path
from apiapp.views import api  # Импорт Ninja API
from django.http import HttpResponse  # Импорт для главной страницы

def home(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', home),  # <-- Главная страница
]

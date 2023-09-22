from django.urls import path
from .views import home_view, about_view

app_name = 'tavreli'

urlpatterns = [
    # URL-адрес для главной страницы
    path('', home_view, name='home'),
    # URL-адрес для страницы "О себе"
    path('about/', about_view, name='about'),
]

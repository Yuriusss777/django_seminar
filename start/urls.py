from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # URL-адрес для включения URL-адресов вашего приложения `tavreli`
    path('', include('tavreli.urls')),
    # URL-адрес для административной панели Django
    path('admin/', admin.site.urls),
]

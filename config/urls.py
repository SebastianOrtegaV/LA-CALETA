
from django.contrib import admin
from django.urls import path
from caleta import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('catalogo/<str:cat>', views.catalogo, name='catalogo'),
]

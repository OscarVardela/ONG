from django.urls import path
from .views import home, galeria, contacto

urlpatterns = [
    path('',home,name= 'index'),
    path('galeria/',galeria, name = 'galeria'),
    path('contacto/',contacto, name= 'contacto')
]

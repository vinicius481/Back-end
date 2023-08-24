from django.urls import path
from galeria.views import index, imagem

imag= 'imagem.html/'

urlpatterns= [
    path('',index),
    path(imag, imagem),
]


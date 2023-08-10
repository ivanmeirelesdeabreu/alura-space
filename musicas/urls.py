from django.urls import path, include
from musicas.views import index 


urlpatterns = [
    path('', index, name='index'),
    
    ]
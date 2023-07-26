from django.urls import path, include
from galeria.views import index


urlpatterns = [
    path('', index)
    ]
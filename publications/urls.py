from django.urls import path
from .views import list_of_publications

urlpatterns = [
    path('all/', list_of_publications),
]
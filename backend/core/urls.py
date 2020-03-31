from django.urls import path
from core.views import all_cars

urlpatterns = [
    path('cars/', all_cars),
]

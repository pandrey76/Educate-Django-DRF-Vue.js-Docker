from django.urls import path

from backend.core.views import all_cars

urlpatterns = [
    path('cars/', all_cars),
]

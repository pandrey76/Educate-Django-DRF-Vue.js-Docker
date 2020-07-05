from django.urls import path
from rest_framework.routers import DefaultRouter
from core.views import CarViewSet

router = DefaultRouter()
# Говорим о том, что у нас по "/api/cars", ну api у нас берётся из "backend/project/urls.py"
# path('api/', include("core.urls")),
# потом cars к api преплюсовываеся и мы хотим отдавать этот .
router.register("cars",CarViewSet)

urlpatterns = router.urls

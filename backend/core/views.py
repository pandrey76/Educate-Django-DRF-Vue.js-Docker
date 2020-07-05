from rest_framework.viewsets import ModelViewSet
from core.models import Car
from core.serializers import CarSerializer


# ModelViewSet даёт нам стандартизированный доступ в стиле REST ко всему вообще. мы можкм
class CarViewSet(ModelViewSet):
    # Мы можем с помощью этого "ModelViewSet" определив класс сериализатора
    serializer_class = CarSerializer
    # и queryset
    queryset = Car.objects.all()

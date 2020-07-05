from rest_framework.serializers import ModelSerializer
from core.models import Car


class CarSerializer(ModelSerializer):
    class Meta:
        # Объявляем какую модель мы хотим сериализовать
        model = Car
        # И какие поля из неё мы хотим сериализовать, обычно это передаётся списком
        # fields = ["vendor", "model", "year", "volume"], но во время разработки, когда у нас API ещё не закреплён и
        # нам надо быстро всё сделать мы можем написать просто: fields = "__all__", это значит все поля модели
        # будут сериализованы.
        fields = "__all__"
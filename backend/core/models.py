from django.db import models

# Create your models here.


class Car(models.Model):
    """

    """
    # Марка производителя
    vendor = models.CharField(max_length=128)
    # Модель
    model = models.CharField(max_length=128)
    # Год
    year = models.PositiveSmallIntegerField()
    #   Гибкость ORM заключается в том , что например в Postgress под тип "PositiveSmallIntegerField" выделится 2 байта,
    #   а в SQLight 4 байта, но для нас в коде это всё будет выглядеть одинаково. ORM сам решает как рпаботать с той
    #   или иной СУБД.

    # Объем двигателя.
    volume = models.PositiveSmallIntegerField()


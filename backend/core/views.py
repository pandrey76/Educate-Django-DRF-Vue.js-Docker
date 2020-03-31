from django.http import JsonResponse

from core.models import Car


def all_cars(request):
    # Нам надо взять все машины, машины получаются так, у каждой модели Django есть мэнаджер , как минимум один
    # дефолтгый менаджер "objects". Мэнаджеры это репозитории или контейнеры, которые могут отдавать какие, то объеты
    # для фильтрации
    result = []
    cars = Car.objects.all()

    # Django не даст нам возвратить масив из-за уязвимостей JSON, поэтому мы пишем save=False, говоря тем самым
    # делвай так.
    # Здесь нам надо пройти по всем нашим машинам со всеми  их характеристиками, закинуть их в словарь, закинуть это
    # словарь в result.
    for car in cars:
        result.append({
            "vendor": car.vendor,
            "model": car.model,
            "year": car.year,
            "volume": car.volume,
        })

    return JsonResponse(result, safe=False)

from django.shortcuts import render, HttpResponse
from . models import Category, Equipment


def index(request):
    equip = Equipment.objects.all()
    data = {'title': 'Главная страница',
               'cats': Category.objects.all(),
               'equip': equip}
    return render(request, 'equipment/index.html', context=data)



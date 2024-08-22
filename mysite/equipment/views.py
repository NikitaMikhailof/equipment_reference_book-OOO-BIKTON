from django.shortcuts import render, HttpResponse
from . models import Category, Equipment


def index(request):
    posts = Equipment.objects.all()
    data = {'title': 'Главная страница',
               'cats': Category.objects.all(),
               'posts': posts}
    return render(request, 'equipment/index.html', context=data)



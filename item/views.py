from django.shortcuts import render

from .models import Item, Photo


def home(request):
    photo = Photo.objects.get(pk=2)
    context = {
        'photo': photo,
    }
    return render(request, 'item/index.html', context)

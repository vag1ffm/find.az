from django.shortcuts import render
from .models import Items


def shop(request):
    items = Items.objects.all()
    return render(request, 'mainpage/index.html', {"items": items})

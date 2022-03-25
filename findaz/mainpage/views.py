from django.shortcuts import render

def shop(request):
    return render(request, 'mainpage/shop.html')

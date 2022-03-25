from django.shortcuts import render

def shop(request):
    return render(request, 'mainpage/index.html')

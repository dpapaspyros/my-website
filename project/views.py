from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def stavel(request):
    return render(request, 'stavel.html')


def info(request):
    return render(request, 'info.html')

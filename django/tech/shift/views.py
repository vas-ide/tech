from django.shortcuts import render


def index(request):
    content = {}
    return render(request, '/', content)


def shift(request):
    content = {}
    return render(request, 'shift/', content)

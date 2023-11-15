from django.shortcuts import render


def index(request):
    content = {}
    return render(request, 'shift/index.html', content)


def shift(request):
    content = {}
    return render(request, 'shift/shift.html', content)

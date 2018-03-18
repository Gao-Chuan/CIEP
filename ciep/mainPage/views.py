from django.shortcuts import render


def home(request):
    boards = [
        {'name': '加密', 'link': '/encrypt'},
        {'name': '认证', 'link': '/authenticate'},
        {'name': 'padding & safe mode', 'link': '/pns'}
    ]
    return render(request, 'index.html', {'boards': boards})

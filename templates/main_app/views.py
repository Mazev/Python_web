from django.shortcuts import render


def index(reg):
    return render(reg, 'main_app/index.html')

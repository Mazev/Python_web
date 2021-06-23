from django.shortcuts import render


def index(reg):
    return render(reg, 'secondary_app/index.html')

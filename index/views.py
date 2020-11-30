# Create your views here.

# from .form import PersonInfoForm
from django.shortcuts import render


def index(request):
    value = {'name': 'Hello Python'}
    return render(request, 'index.html', locals())

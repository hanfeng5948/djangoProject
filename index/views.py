# Create your views here.

from django.shortcuts import render

from .form import *


def index(request):
    v = lmForm()
    s = sminfoForm()
    return render(request, 'index.html', locals())

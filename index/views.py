# Create your views here.

# from .form import PersonInfoForm
from django.shortcuts import render
from django.views.generic import ListView
from .models import lm
from django.db.models import Max, Min


class index(ListView):
    template_name = 'index.html'
    queryset = lm.objects.order_by('lmcode')
    extra_context = {'value': '栏目表'}

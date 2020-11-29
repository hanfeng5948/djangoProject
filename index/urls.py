from django.urls import re_path, path
from .views import *

urlpatterns = [
    path('<int:year>/<int:week>.html', index.as_view(), name='index')
    # path('', index.as_view(), name='index'),
    # path('result', result, name='result')
]

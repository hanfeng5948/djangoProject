from django.apps import AppConfig
import os


class IndexConfig(AppConfig):
    name = os.path.split(os.path.dirname(__file__))[-1]
    verbose_name = '网站首页'

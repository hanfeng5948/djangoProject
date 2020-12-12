from django import forms
from django.core.exceptions import ValidationError
from .models import *


class PersonInfoForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = '__all__'


def cho_db(db, filed, label):
    lst = db.objects.values(filed).order_by(filed).distinct()
    cho = [(i + 1, ch[filed]) for i, ch in enumerate(lst)]
    filed = forms.ChoiceField(choices=cho, label=label)
    return filed


class lmForm(forms.Form):
    lmoldcode = forms.IntegerField(label='旧编码', )
    lmtitle = forms.CharField(max_length=32, label='名称')
    lmcode = forms.CharField(max_length=27, label='新编码')
    lmlv = cho_db(lm, 'lmlevel', '层级')

    # level = lm.objects.values('lmlevel').order_by('lmlevel').distinct()
    # choices = [(i+1, l['lmlevel']) for i, l in enumerate(level)]
    # lmlevel = forms.ChoiceField(choices=choices, label='层级')


class sminfoForm(forms.Form):
    title = forms.CharField(max_length=32, label='名称')
    uptime = forms.DateTimeField(widget=forms.widgets.DateTimeInput())

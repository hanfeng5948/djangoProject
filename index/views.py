# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .form import PersonInfoForm

class index(FormView):
    initial = {'name':'Betty', 'age':'30'}
    template_name = 'index.html'
    success_url = '/result'
    form_class = PersonInfoForm
    extra_context = {'title':'PERSON INFO'}

def result(request):
    return HttpResponse('success')

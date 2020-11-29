# Create your views here.
from django.http import HttpResponse
from django.views.generic.dates import WeekArchiveView

# from .form import PersonInfoForm
from .models import PersonInfo


class index(WeekArchiveView):
    # initial = {'name': 'Jack', 'age': '22'}
    allow_empty = True
    allow_future = False
    template_name = 'index.html'
    model = PersonInfo
    context_object_name = 'mylist'

    date_field = 'hireDate'
    queryset = PersonInfo.objects.all()

    year_format = '%Y'
    week_format = '%W'
    # month_format = '%m'

    paginate_by = 3
    # success_url = '/result'
    # form_class = PersonInfoForm
    # model = PersonInfo
    # fields = ['name', 'age', 'hireDate']
    # slug_url_kwarg = 'age'
    # slug_field = 'age'
    extra_context = {'title': 'PERSON INFO'}


def result(request):
    return HttpResponse('success')

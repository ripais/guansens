from django.shortcuts import render
from forms import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.template import RequestContext
from chartit import DataPool, Chart
from django.shortcuts import render_to_response
from .models import DataTable
from .models import Event
from django.views.generic import DayArchiveView
from django.views.generic import MonthArchiveView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return render(request, "logout.html")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            return HttpResponseRedirect('registration/registration_complete.html')
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render(request, 'registration/registration_form.html', {'form': form})

login_required(login_url="login/")
def sensor_chart_view(request):
    graph1 = DataTable.objects.filter(actual__gt = datetime.date(2017, 03, 17))
    print graph1.query
    ds = DataPool(
        series=[{
            'options': {
                'source': graph1
            },
            'terms': [
                'value',
                'actual',
            ]
        }]
    )

    cht = Chart(
        datasource=ds,
        series_options=[{
            'options': {
                'type': 'line',
                'stacking': False
            },
            'terms': {
                'actual': [
                    'value'
                ]
            }
        }],
        chart_options={
            'title': {
                'text': 'Altura del canal'
            },
            'xAxis': {
                'title': {
                    'text': 'fecha'
                }
            },
            'credits': {
                'enabled': True,
                'text': 'GUANCHIP',
                'href': 'http://guanchip.com'
            }
        },
        x_sortf_mapf_mts=(None, None, False))
        #x_sortf_mapf_mts=(None, lambda i: datetime.fromtimestamp(float(i)).strftime('%H:%M'), False))
    # end_code
    return render_to_response('sensor_chart_view.html', {'chart_list': cht, })

class EventosDia(DayArchiveView):
    queryset = Event.objects.order_by('time')
    template_name = 'eventos_dia.html'
    date_field = 'time'
    context_object_name = 'eventos'
    month_format = '%m'

class EventosMes(MonthArchiveView):
    queryset = Event.objects.order_by('fecha')
    template_name = 'eventos_mes.html'
    date_field = 'time'
    month_format = '%m'
    context_object_name = 'eventos'
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^logout/$', logout, {'next_page':'/login'}),
    url(r'^register/', views.register, name='register'),
    url(r'^index/', views.index, name='index'),
    url(r'^sensor_chart_view/', views.sensor_chart_view, name='sensor_chart_view'),
    url(r'^calendar/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})$',views.EventosDia, name='entradas'),
    url(r'^EventosMes/(?P<year>\d{4})/(?P<month>\d{2})/$',views.EventosMes, name='entradas'),
]

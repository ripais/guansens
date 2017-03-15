from django.contrib import admin

# Register your models here.
from models import RaspTable
from models import UsersRasp
from models import SensorTable
from models import DataTable
from models import Event

admin.site.register(RaspTable)
admin.site.register(UsersRasp)
admin.site.register(SensorTable)
admin.site.register(DataTable)
admin.site.register(Event)
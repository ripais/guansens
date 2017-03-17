from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class RaspTable(models.Model):
    id_rasp = models.AutoField(primary_key=True)
    numsensor = models.IntegerField(u'Numero sensores')
    localaddress = models.CharField(u'LAN IP', max_length=15)
    connectionhost = models.CharField(u'WAN IP', max_length=15)
    port = models.IntegerField(u'Port')
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return '%s:%s' % (self.connectionhost, self.port)


class UsersRasp(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    id_rasp = models.ForeignKey(RaspTable, on_delete=models.CASCADE, default=None)

    def __unicode__(self):
        return '%s - %s' % (self.user.username, self.rasp)

class Event(models.Model):
    id_event = models.AutoField(primary_key=True)
    name = models.CharField(u'Name', max_length=100)
    description = models.CharField(u'Description', max_length=255)
    id_user = models.ForeignKey(UsersRasp, on_delete=models.CASCADE,default=None)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    repeat_after = models.IntegerField(default=0)
    trigger = models.BooleanField(default=None)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.time)

class SensorTable(models.Model):
    id_sensor = models.AutoField(primary_key=True)
    id_rasp= models.ForeignKey(RaspTable, on_delete=models.CASCADE, default=None)
    msensor = models.CharField(max_length=8)
    located = models.CharField(max_length=32)
    address = models.CharField(max_length=15)
    port = models.IntegerField()
    nserie = models.CharField(max_length=13)
    nmodel = models.CharField(max_length=8)
    nfirm = models.CharField(max_length=8)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return '%d %s %s' % (self.id_sensor, self.msensor, self.address)


class DataTable(models.Model):
    id_datatable = models.AutoField(primary_key=True)
    value = models.FloatField()
    fecha = models.FloatField(blank=True, null=True)
    actual = models.DateTimeField(blank=True, null=True)
    metrica = models.IntegerField()
    numsensor = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    sensor  = models.ForeignKey(SensorTable, on_delete=models.CASCADE, default=None)

    def __unicode__(self):
        return '%d %s' % (self.value, self.fecha)

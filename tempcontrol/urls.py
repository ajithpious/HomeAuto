from django import views
from django.urls import path
from tempcontrol.views import command

from tempcontrol.views import home
from tempcontrol.views import home,getStatus
urlpatterns = [ path('',home),
path('getstatus',getStatus),
path('command',command)
]
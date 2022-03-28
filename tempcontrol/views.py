from django.http import HttpResponse
from django.shortcuts import render
import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish

# Create your views here.
def home(request):
    return render(request,"home.html")
def getStatus(request):
    msg=subscribe.simple("/v1.6/devices/esp32/temp",msg_count=1, hostname="industrial.api.ubidots.com",
    port=1883, client_id="12345", keepalive=60, will=None, auth = {'username':"BBFF-Bfw8lO95m9pzKw8zE0Zupzw5OrKDQ0", 'password':""})
    print(msg.payload)
    return HttpResponse(msg.payload)
def command(request):
    val=request.GET.get('value',None)
    print(val)
    msg=publish.single("/v1.6/devices/esp32/command",val, qos=1,retain=False, hostname="industrial.api.ubidots.com",
    port=1883, client_id="1563", keepalive=60, will=None, auth = {'username':"BBFF-Bfw8lO95m9pzKw8zE0Zupzw5OrKDQ0", 'password':""})
    print("mssge=",msg)
    return HttpResponse(b'{"status": "success"}')

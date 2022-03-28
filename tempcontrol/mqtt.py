import paho.mqtt.client as mqtt

token="BBFF-Bfw8lO95m9pzKw8zE0Zupzw5OrKDQ0"
data=""
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
        client.bad_connection_flag=True
    client.subscribe("$SYS/#")
    client.subscribe("/v1.6/devices/esp32/temp")

def on_message(client, userdata, msg):
    print(msg.payload)
    print("dfdv")
    pass


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username=token,password="")

client.connect("industrial.api.ubidots.com", 1883, 60)
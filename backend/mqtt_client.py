import json
import paho.mqtt.client as mqtt

from geofence import check_geofence
from logger import save_record

BROKER = "broker.hivemq.com"

TOPIC = "vehicle/location"

def on_message(
        client,
        userdata,
        msg):

    data = json.loads(msg.payload)

    lat = data["lat"]
    lon = data["lon"]

    alert = "SAFE"

    if check_geofence(lat,lon):

        alert = "GEOFENCE ALERT"

    save_record(
        lat,
        lon,
        "MOVING",
        alert
    )

    print(alert)

client = mqtt.Client()

client.connect(
    BROKER,
    1883
)

client.subscribe(TOPIC)

client.on_message = on_message

client.loop_forever()
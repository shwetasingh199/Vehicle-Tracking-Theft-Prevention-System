import pandas as pd
import paho.mqtt.client as mqtt
import time
import json

broker = "broker.hivemq.com"
topic = "vehicle/location"

client = mqtt.Client()
client.connect(broker,1883)

data = pd.read_csv("routes.csv")

while True:

    for _,row in data.iterrows():

        payload = {
            "lat":float(row["latitude"]),
            "lon":float(row["longitude"]),
            "status":"MOVING"
        }

        client.publish(topic,json.dumps(payload))

        print(payload)

        time.sleep(3)
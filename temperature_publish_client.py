import paho.mqtt.client as mqtt
import time, random

mqttc = mqtt.Client("temperature_pub")
# MQTT client object create
mqttc.connect("127.0.0.1", 1883)
# MQTT server connect

while 1:
	temperature = random.randint(20, 35)
	mqttc.publish("environment/temperature", temperature)
	print "Temperature : " + str(temperature)
	time.sleep(2)
	mqttc.loop(2)


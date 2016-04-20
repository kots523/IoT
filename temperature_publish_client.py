import paho.mqtt.client as mqtt
import time, random
#import time and random function

mqttc = mqtt.Client("temperature_pub")
# MQTT client object create
mqttc.connect("127.0.0.1", 1883)
# MQTT server connect

while 1:
	temperature = random.randint(20, 35)
	#init temperature data by random (range : 20 ~ 35)
	mqttc.publish("environment/temperature", temperature)
	print "Temperature : " + str(temperature)
	time.sleep(2)
	#wait 2 second
	mqttc.loop(2)


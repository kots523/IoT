import paho.mqtt.client as mqtt
import time, random
#import time and random function

mqttc = mqtt.Client("humidity_pub")
# MQTT client object create
mqttc.connect("127.0.0.1", 1883)
# MQTT server connect

while 1:
	humidity = random.randint(30, 95)
	#init humidity data by random (range : 30 ~ 95)
	mqttc.publish("environment/humidity", humidity)
	print "Humidity : " + str(humidity)
	time.sleep(2)
	#wait 2 second
	mqttc.loop(2)


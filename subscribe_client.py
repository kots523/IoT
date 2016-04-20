import paho.mqtt.client as mqtt
T = 0; RH = 0; T_new = 0; RH_new = 0;
#init variable

#callback if receive CONNACK answer by client_server
def on_connect(client, userdata, rc):
	print ("Connected with result coe " + str(rc))
	client.subscribe("environment/temperature")
	client.subscribe("environment/humidity")

# callback if receive PUBLISH message by server
def on_message(client, userdata, msg):
	global T, RH, T_new, RH_new
	#use global variable

	if msg.topic == "environment/temperature":
		T = float(msg.payload)
		T_new = 1
	elif msg.topic == "environment/humidity":
		RH = float(msg.payload)
		RH_new = 1
	#if receive publish data, then init data and checksum
	
	if (T_new == 1) and (RH_new == 1):
		result = (9.0 / 5.0 * T) - (0.55 * (1 - (RH / 100.0)) * (9.0 / 5.0 * T - 26)) + 32
		#Calculate discomfort index, Humidity value dividing by 100(percentage)

		print "Temperature : " + str(T) + ", Huminity : " + str(RH) + " %"
		print "Discomfort index : " + str(result),
		if (result >= 80):
			print " (Very High)\n"
		elif (result >= 75) and (result < 80):
		 	print " (High)\n"
		elif (result >= 68) and (result < 75):
			print " (Medium)\n"
		else:
		 	print " (Low)\n"
		#return discomfort index
		T_new = 0; RH_new = 0;
		#init checksum variable

client = mqtt.Client()	# MQTT Client object create
client.on_connect = on_connect	# on_connect callback create
client.on_message = on_message	# on_message callback create

client.connect("127.0.0.1", 1883, 60)	# MQTT server connect

client.loop_forever()

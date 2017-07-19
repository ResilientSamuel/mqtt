from gpiozero import LED
from time import sleep
import paho.mqtt.client as mqtt

led = LED(17)


def dot():
        led.on()
        sleep(1)
        led.off()
        sleep(1)

def dash():
         led.on()
         sleep(2)
         led.off()
         sleep(2)


def on_message(client, userdata, message):
        print message.payload
	dot()
	dash()
	

def password (Apologist):
	if on_message:

 		  print password "Apologist"
 		  print on_message
	else:
   		print " Got a false expression "
   		print on_message

def on_connect(client, userdata, flags, code):
        print "connected: " + str(code)
        client.subscribe("test/ResilientSamuel")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("moorhouseassociates.com", 1883, 60)

client.loop_forever()



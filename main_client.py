from bluetooth import *
from connection_util import *

import pyupm_i2clcd as lcd
import pyupm_grove as grove

import time

LCD = lcd.Jhd1313m1(0, 0x3E, 0x62)
button = grove.GroveButton(2)

def walking():
	LCD.clear()
	LCD.setCursor(0,0)
	LCD.write("Andando...")

	i = 10
	time_color = time.time()

	while not button.value():
		# print button.name(), ' value is ', button.value()
		LCD.setColor(50, 50, i)
		if (time_color + 0.3 < time.time()):
			i = i % 200 + 25
			time_color = time.time()

def init():
	manage_connection(True)
	
def main():
	addr = None	

	# search for the SampleServer service
	uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
	addr = "98:4F:EE:03:7D:27"
	print("finding")

	service_matches = find_service( uuid = uuid, address = addr )

	if len(service_matches) == 0:
		print("couldn't find the SampleServer service =(")
		sys.exit(0)

	first_match = service_matches[0]
	port = first_match["port"]
	name = first_match["name"]
	host = first_match["host"]

	print("connecting to \"%s\" on %s" % (name, host))
	LCD.clear()
	LCD.setCursor(0,0)
	LCD.setColor(0, 0, 100)
	LCD.write("Conectado a " + name)

	# Create the client socket
	sock=BluetoothSocket( RFCOMM )
	sock.connect((host, port))

	print("connected.  type stuff")
	while not button.value():
		data = input()
		if len(data) == 0: break
		sock.send(data)
		data = client_sock.recv(1024)
		if len(data) == 0: break

	sock.close()


if __name__ == '__main__':
	init()

	while True:
		walking()
		main()
	
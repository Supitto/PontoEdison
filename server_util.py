#!/usr/bin/env python 
import ponto
from bluetooth import *
import pyupm_i2clcd as lcd
import time
from datetime import datetime
import requests, json
from time import gmtime, strftime

LCD = lcd.Jhd1313m1(0, 0x3E, 0x62)

def init():
	#LCD = lcd.Jhd1313m1(0, 0x3E, 0x62)
	pass

def fetch_bus(ponto):
	LCD.clear()
	LCD.setCursor(0,0)
	LCD.setColor(0, 0, 100)
	LCD.write("Conectando...")
	
	r = requests.get('http://marcomini.com.br/API/onibus/'+ponto.ponto_id)
	print(r.json())

	LCD.setCursor(1,0)
	LCD.write("OK")

def run_server():
	LCD.clear()
	LCD.setCursor(0,0)
	LCD.setColor(0, 100, 0)
	LCD.write("Procurando...")

	server_sock = BluetoothSocket(RFCOMM)
	server_sock.bind(("",PORT_ANY))
	server_sock.listen(1)

	port = server_sock.getsockname()[1]

	uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

	advertise_service( server_sock, "Ponto Edison",
					   service_id = uuid,
					   service_classes = [ uuid, SERIAL_PORT_CLASS ],
					   profiles = [ SERIAL_PORT_PROFILE ], 
	#                   protocols = [ OBEX_UUID ] 
					   )
					   
	print("Waiting for connection on RFCOMM channel %d" % port)

	client_sock, client_info = server_sock.accept()
	print("Accepted connection from ", client_info)

	LCD.clear()
	LCD.setCursor(0,0)
	LCD.setColor(0, 100, 100)
	LCD.write("Conectado a")
	LCD.setCursor(1,0)
	LCD.write(str(client_info[0]))

	try:
		url = "http://marcomini.com.br/API/Log/%s/%s/'%s'"
		

		r = requests.get(url%(1, 1, strftime("%X", gmtime())))


		print r.json
		while True:
			pass
		# 	data = client_sock.recv(1024)
		# 	if len(data) == 0: break
		# 	print("received [%s]" % data)
	except IOError:
		pass

	print("disconnected")

	client_sock.close()
	server_sock.close()
	print("all done")

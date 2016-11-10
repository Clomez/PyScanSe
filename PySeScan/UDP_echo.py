#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
from time import sleep

def UDP():
	address = 'localhost'
	port = 10000
	message = "This is a message, hello!"

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	ask = raw_input("Give port: ")
	port = ask
	port = int(port)
	ask = raw_input("Give address: ")
	address = ask
	try:

		#send data
		print ("sending data")
		sent = sock.sendto(bytes(message),(address, port))
		sock.settimeout(5.0)

		#receive response
		data = sock.recvfrom(4096)
		print (data)

	except socket.timeout as err:
		print("Connection timed out...\n")

	finally:
		print ("closing socket")
		sock.close()
if __name__ == "__main__":
	UDP()


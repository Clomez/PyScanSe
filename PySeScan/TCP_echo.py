#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
from time import sleep

address = 'localhost'
port = 80
message = "2222"

def mainTCP_m():
	ask = raw_input("Give address: ")
	address = ask
	ask = raw_input("Give port: ")
	port = ask
	port = int(port)
	ask = raw_input("Give message: ")
	message = ask

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		#conenct
		sock.connect((address, port))
		#send data
		print ("sending data")
		sent = sock.send(bytes(message))
		sleep(1)
		sock.settimeout(5.0)

	
		#receive response
		data = sock.recv(1024)
		print ("Receied data: " , data)

	except socket.error, e:
		if 'Connection refused' in e:
		    print '*** Connection refused ***'

	finally:
		print ("closing socket")
		sock.close()
if __name__ == "__main__":
	main()


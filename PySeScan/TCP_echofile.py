#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
from time import sleep

def main():
	reader = raw_input("Give address: ")
	address = reader
	reader = raw_input("Give Port: ")
	portin = reader
	port = int(portin)
	reader = raw_input("Give File name: ")
	messageraw = open(reader, "r")
	message = messageraw.read()

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		#conenct
		sock.connect((address, port))
		#send data
		print ("sending data")
		sent = sock.send(message)
		sleep(1)

		#receive response
		data = sock.recv(1024)
		if not data:
			print ("no response :(")
		print ("Receied data: " , data)

	finally:
		print ("closing socket")
		sock.close()
if __name__ == "__main__":
	main()


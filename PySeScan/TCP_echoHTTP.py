#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
from time import sleep

def main():
	ask = raw_input("Give address: ")
	address = ask
	ask = raw_input("Give port:  // 80 for HTTP")
	port = ask
	port = int(port)
	CRLF = "\r\n\r\n"

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		#conenct
		sock.connect((address, port))
		#send data
		print ("sending data")
		sent = sock.send("GET / HTTP/1.0%s" % (CRLF))
		sleep(1)

		#receive response
		data = sock.recv(100000)
		if not data:
			print ("no response :(")
		print ("Receied data: " , data)

	finally:
		print ("closing socket")
		sock.close()
if __name__ == "__main__":
	main()


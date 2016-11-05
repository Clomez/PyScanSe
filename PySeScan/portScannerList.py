#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from errno import ECONNREFUSED
from functools import partial
from multiprocessing import Pool
import socket
import os
import sys



def ping(host, port):
	#kokeile socket
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		print(str(port) + " Open")
		return port
	except socket.error as err:
		if err.errno == ECONNREFUSED:
			return False
		raise
def scan_ports(host, port):
	ping_host = partial(ping, host)
	return filter(ping_host, range(1, 65536))

def main():


	reader = raw_input("Give target list: ")
	f = reader
	portin = 2
	port = int(portin)
	BUFFER_SIZE = 1024
	message = "test"
	#reader = raw_input("Give Port: ")
	with open(f) as fp:
		for line in fp:
			currentline = line.split(",")
			StrL = str(currentline)
			if "//" in StrL:
				pass
			else:
				host = StrL.replace("\\n","")
				host = host.replace("[","")
				host = host.replace("]","")
				host = host.replace("'","")

				print("\nScanning ports on " + host + " ...")
				ports = list(scan_ports(host, port))
				print("\nDone.")

				print(str(len(ports)) + " ports available.")
				print(ports)

if __name__ == "__main__":
	main()

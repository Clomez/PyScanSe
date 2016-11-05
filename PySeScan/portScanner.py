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

	reader = raw_input("Give address: ")
	host = reader
	#reader = raw_input("Give Port: ")
	portin = 2
	port = int(portin)
	BUFFER_SIZE = 1024
	message = "test"
	if host is None:
		host = "127.0.0.1"

	print("\nScanning ports on " + host + " ...")
	ports = list(scan_ports(host, port))
	print("\nDone.")

	print(str(len(ports)) + " ports available.")
	print(ports)

if __name__ == "__main__":
	main()

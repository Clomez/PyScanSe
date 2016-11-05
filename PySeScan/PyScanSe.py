#!/usr/bin/python      
# -*- coding: utf-8 -*-
from errno import ECONNREFUSED
from functools import partial
from multiprocessing import Pool
import socket
import os
import sys
import UDP_echo
import portScanner
import PyFTP
import TCP_echofile
import TCP_echoHTTP
import portScannerList


def main2():
	reader = "22"
	while True:

		
		print ("\n\n-------------------------------------")
		print(" PyScanSe ++ ver0.5")
		print("------------------------------------ ")
		print("   MENU ")
		print("1. Port scanner ")
		print("2. Send UDP packages")
		print("3. Send TCP short message")
		print("4. Send TCP package from file")
		print("5. Send TCP HTTP GET")
		print("-------------------------------------")
		print("6. Port scanner // use target list")
		print("-------------------------------------")
		print("7. FTP BruteForce using file // user & pass ")
		print("-------------------------------------")
		print("c. Credits")
		print("h. Help")
		print("0. Exit")
		print("-------------------------------------\n")
		reader = raw_input("> ")

		if reader == "1":
			portScanner.main()
			raw_input("\nPress Enter to continue...")
			main2()
		if reader == "2":
			UDP_echo.UDP()
			raw_input("\nPress Enter to continue...")
			main2()
		if reader == "3":
			TCP_echo.mainTCP_m()
			raw_input("\nPress Enter to continue...")
			main2()
		if reader == "4":
			TCP_echofile.main()
			raw_input("\nPress Enter to continue...")
			main2()
		if reader == "5":
			TCP_echoHTTP.main()
			raw_input("\nPress Enter to continue...")
			main2()
		if reader == "6":
			portScannerList.main()
			raw_input("\nPress Enter to continue...")
			main2()
		if reader =="7":
			PyFTP.main()
			raw_input("\nPress Enter to continue...")
			main2()
		if reader =="c":
			messageraw = open("credits", "r")
			message = messageraw.read()
			print(message)
			raw_input("\nPress Enter to continue...")
			main2()
		if reader =="h":
			messageraw = open("help", "r")
			message = messageraw.read()
			print(message)
			raw_input("\nPress Enter to continue...")
			main2()
		if reader == "0":
			exit()
if __name__ == "__main__":
	main2()

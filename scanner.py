#!/bin/python3
import sys #allows to enter cmd line arguments
import socket 
from datetime import datetime

#Define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate host name to IP address
else:	
	print("Invalid amount of arguments")
	sys.exit()

print("-" * 50)
print("Scanning target is "+target)
print("Time started is "+str(datetime.now()))
print("-" * 50)

try:
	for port in range (50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		print("checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
	
except KeyboardInterrupt:
	print("\n Exiting program")
	sys.exit()

except socket.gaierror:
	print("socket name cannot resolved")
	sys.exit()

except socket.error:
	sys.exit()
			
















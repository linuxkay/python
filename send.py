#!/usr/local/bin/python
import socket
UDP_IP = "10.8.0.6"
UDP_PORT = 1194
MESSAGE = "findsomemotion"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


#!/usr/bin/env/python
#
# Peer
#
from socket import *

BROKER_HOST = "192.168.11.3"
BROKER_PORT =  8081 
BROKER_ADDR = (BROKER_HOST, BROKER_PORT)

sock = socket(AF_INET, SOCK_DGRAM)
# to support two peers on the same machine
try:
   sock.bind(('', 9900))
except:
   sock.bind(('', 9901))

sock.sendto("ping", BROKER_ADDR)

while 1:
   data, addr = sock.recvfrom(128)
   new_data = data.split()
   if new_data[0] == "peer":
       addr = new_data[1]
       port = int(new_data[2])
       sock.sendto("resp test", (addr, port))
   elif new_data[0] == "resp":
       sock.sendto("what goes around comes around", addr)
   print addr, data

#!/usr/bin/env/python
#
# Broker
#
from socket import *
import socket
HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

peers = {}

while 1:
   data, addr = s.recvfrom(128)
   print addr, data
   peers[addr] = True
   if len(peers) > 1:
       peer1 = peers.keys()[0]
       peer2 = peers.keys()[1]
       s.sendto("peer " + peer2[0] + " " + str(peer2[1]), peer1)
   else:
       s.sendto("pong", addr)

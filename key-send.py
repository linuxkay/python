#!/usr/env/bin/python
import sys
import socket
import paramiko
def getStatus():
    ip=''
    port=
    username=''
    password=''
    cmd='ls'
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,username,password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    outlines=stdout.readlines()
    resp=''.join(outlines)
    print(resp)
def sendCommand():
    UDP_IP = ""
    UDP_PORT = 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(command, (UDP_IP, UDP_PORT))
def getUserResponse():
    return raw_input("\nOrder?\n> ")
while True:
  print "----Obtaining Status of Name ----\n> ", getStatus()
  mode = getUserResponse()
  if mode in ["","",""]:
      command = ""
      sendCommand()
  elif mode in ["","",""]:
      command = ""
      sendCommand()
  elif mode in ["","",""]:
      command = ""
      sendCommand()
  elif mode in ["",""]:
      command = ""
      sendCommand()
  elif mode in ["",""]:
      command = ""
      sendCommand()
  else:
    print "Invalid input"

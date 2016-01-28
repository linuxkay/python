import socket

UDP_IP = "10.8.0.6"
UDP_PORT = 1194

sock = socket.socket(socket.AF_INET, # Internet
		     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    f = open('word.txt', 'r+')
    f.write(data)
    f.close()

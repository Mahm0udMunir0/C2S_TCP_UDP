#!/bin/python3
# UDP client

# Import Libraries
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "Hello UDP SERVER"
sock.sendto(msg.encode(), ("127.0.0.1", 12345))
data, addr = sock.recvfrom(4096)
print("Server Says")
print(str(data))
sock.close()


#!/bin/python3
# UDP server

# Import Libraries
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 12345))

while True:
    data, addr = sock.recvfrom(4096)
    message_received = data.decode()
    print(f"Received from {addr}: {message_received}")

    response = f"Hello, {message_received}!"
    sock.sendto(response.encode(), addr)
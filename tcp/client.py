#!/bin/python3
# TCP/IP Client

# Import Libraries
import socket

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 7070)
print('connecting to %s port %s' % server_address)
Socket.connect(server_address)

try:
    # Send data
    message = 'this is a message, please repeat'
    print('sending %s' % message)
    Socket.sendall(bytes(message, 'utf-8'))

    # Look for response back
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = Socket.recv(1600)
        amount_received += len(data)
        print('received %s' % data)

finally:
    print('closing client')
    Socket.close()

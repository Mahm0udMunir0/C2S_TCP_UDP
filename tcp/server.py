#!/bin/python3
#TCP/IP Server

#import Libraries
import socket
#create a TCP/IP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to the specific for the server
server_address = ('localhost', 7070)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
#listen for inbound connections
sock.listen(1)
while True:
    # wait  for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)
        # receive the data in chunks of bytes
        while True:
            data = connection.recv(1600)
            print('received "%s"' % data)
            if data:
                print('Sending data back to client')
                msg = str(data)
                msg = msg + 'plus extra from server'
                msg = bytes(msg, 'utf-8')
                connection.sendall(msg)
            else:
                print('noo more data', client_address)
                connection.close()
                break
    finally:
        # clean up  the connection
        connection.close()




#!/usr/bin/env python

# TCP server

import socket, sys

host = ''  # bind to all interfaces
port = 54321  # can also use port 80 etc others if run as root

# Step 1: create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # same socket object as for client
                                                       # use AF_INET6 for binding to an IPv6 address

# Step 2: set socket options
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # release the port as soon as process terminates/socket is closed

# Step 3: bind to port and interface/network card
s.bind((host, port))

print "Waiting for connections..."

# Step 4: Listen for connections
s.listen(5)  # 5 is max num of pending connections in queue

while 1:
    clientsock, clientaddr = s.accept()
    print "Got connection from", clientsock.getpeername()
    clientsock.close()

#!/usr/bin/env python

# a simple UDP echo server

import socket, traceback

host = ''  # bind to all interfaces
port = 12345
buffersize = 8192

# create socket, set socket options, bind
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

while 1:
    # FIXME connectionless, doesn't need to create a new socket to send the reply
    # what does that mean exactly?
    try:
        message, address = s.recvfrom(buffersize)
        print "Got data from", address
        # Echo it back
        s.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

#!/usr/bin/env python

# TCP server

import socket, traceback

host = ''  # bind to all interfaces
port = 54321  # can also use port 80 etc others if run as root

# Step 1: create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # same socket object as for client
                                                       # use AF_INET6 for binding to an IPv6 address
                                                       # or AF_UNSPEC to support both

# Step 2: set socket options
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # release the port as soon as process terminates/socket is closed

# Step 3: bind to port and interface/network card
s.bind((host, port))

print "Waiting for connections..."

# Step 4: Listen for connections
s.listen(5)  # 5 is max num of pending connections in queue

# FIXME how do we service multiple clients simultaneously with this?
# Step 5:
while 1:
    # FIXME this spawns a new socket. Is it already enough to service multiple connections
    # at the same time? How is it done? it doesn't seem to spawn a new process (at least not
    # by the current user)
    # FIXME the program is /blocked/ waiting for any client to connect
    # once /any/ client connects, it will __do something__ with a new socket
    # and be blocked again, until another client connects (?)

    # don't let errors terminate the server
    # if there are problems with clients, just ignore them
    # FIXME add logging later

    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue  # return to the top of the loop to listen for the next connection

    try:
        print "Got connection from", clientsock.getpeername()
        # process the request here. it might call sys.exit() which is caught and re-raised
        # in the next except block
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()

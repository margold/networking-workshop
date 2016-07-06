#!/usr/bin/env python

import sys, socket, time

# inetd passes the sockets as stdin and stdout
# you can read from/write to stdin/stdout directly
# abut you can also create a socket object if you want to use socket-specific features
s = socket.fromfd(sys.stdout.fileno(), socket.AF_INET, socket.SOCK_STREAM)
s.sendall("Welcome.\n")
s.sendall("According to our records, you are connected from %s.\n" % str(s.getpeername()))
s.sendall("The local time is %s.\n" % time.asctime())

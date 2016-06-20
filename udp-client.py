#!/usr/bin/env python

# Basic UDP client

import socket, sys

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port = int(textport)
except ValueError:
    # That didn't work. Look it up instead.
    port = socket.getservbyname(textport, 'udp')

s.connect((host, port))
print "Enter data to transmit: "
data = sys.stdin.readline().strip()

try:
    s.sendall(data)
except socket.error, e:
    print "Error sending data: %s" % e
    sys.exit(1)

print "Looking for replies; press Ctrl-C to stop."
while 1:
    try:
        buf = s.recv(2048)
    except socket.error, e:
        print "Error receiving data: %s" % e
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)

#!/usr/bin/env python

# echo TCP client
#
# This client can be used together with the echo server to demonstrate
# deadlock. It attempts to send 10MB of data, and only then reads the
# answer from the server. After a while, the outgoing buffers on both
# ends will fill, and both processes will be stuck in send().

import socket, sys

host = sys.argv[1]
port = int(sys.argv[2])

data = "x"*10485760  # 10MB of data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print "Connected from client", s.getsockname()
print "Connected to server", s.getpeername()

byteswritten = 0
while byteswritten < len(data):
    startpos = byteswritten
    endpos = min(byteswritten + 1024, len(data))
    byteswritten += s.send(data[startpos:endpos])
    sys.stdout.write("Wrote %d bytes\n" % byteswritten)
    sys.stdout.flush()

s.shutdown(1)

print "All data sent."

# the echo part
while 1:
    buf = s.recv(1024)
    if not len(buf):
        break
    sys.stdout.write(buf)

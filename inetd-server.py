#!/usr/bin/env python

import sys

print "Welcome."
print "Please enter a string: "
sys.stdout.flush()  # inetd passes the outgoing socket as stdout to this script
line = sys.stdin.readline().strip()  # inetd passes the incoming socket as stdin to this script
print "You entered %d characters." % len(line)

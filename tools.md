# Tools
telnet
traceroute
dig

# Testing
## TCP Client
`telnet host port`
(also netcat)
## UDP Client
`nc -u host port` (`-u` is for "udp"; to send data, input data and hit Enter)
## TCP Server
netcat/tcpdump
## UDP Server
netcat/tcpdump

# More tools
- list all manpages for a given topic: `man -a -w|--path term`
(for whatever reason, `man -f term` (aka `whatis term`) and `man -k ^term` (aka `apropos ^term`) don't give you everything)

/etc/services holds IANA's list of assigned port numbers

# Sockets
FIXME
tcp server: socket - opts - bind - listen - accept
tcp client: socket - connect - send ?

udp server: socket - opts - bind - recvfrom/sendto

The GNU C Library Reference Manual: http://www.gnu.org/software/libc/manual/html_node/Sockets.html

# inetd/launchd
My inetd-style launchd plist file for `/Users/margold/RC/networking/inetd-server.py` is in `~/Library/LaunchAgents/margold.inetd.server.plist`.
It can be launched with `launchctl load $path` and talked to with `telnet localhost 12345`
Documentation is here: https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html
Some more ideas are here: http://paul.annesley.cc/2012/09/mac-os-x-launchd-is-cool/

# Qs
write same server in a different language? Haskell? Probably for later this week, or the week after
look at socket module documentation

# Thursday
kernel networking security issues mini-talk?

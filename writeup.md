TOC/General structure
From ... up to (not including) HTTP

# Motivation
show server code using urllib2 or requests or similar - what happens under the hood?
also, it will make you understand a bunch of concepts and weird error messages

# First things first: Tools
telnet
traceroute
dig
nc

# Networking
- every machine on a network has an IP address and a netmask (eg. 10.0.0.0/8 or 255.)
- netmask decides whether communication between two machines must go through router
example: ifconfig

# Setting the stage: code
live-code a simple socket server in python (maybe also file I/O) to set the stage for explanation about the C standard library

# C standard library
(sources: GNU C Library Reference Manual)
- different implementations (BSD, Linux, alternative Linux implementations, embedded, ...)
- de-facto part of nix OSs

# Kernel space/User space
??? <= syscalls go here

# Sockets
communication style x namespace -> default protocol

stream      datagram       raw
     *~~ same protocol ~~*          local (unix domain system, file namespace)
 *TCP*      *UDP/RDP*               internet (IPv4, IPv6)

- TCP connections behave like normal files and can be interacted with with normal syscalls (read/write/close) in addition to socket-specific syscalls
- UDP is per-packet, not a stream of bytes

## Addressing
- IPs
- ports

## Local Sockets
- socket addresses are file names (usually in /tmp)
- can only be connected to from the same machine, even if file system is shared by multiple machines
- socket pairs can be used with this namespace (much like a pipe, but bidirectional and with some added functionality)
- permissions on the socket file control who has access to the socket (i.e. who can connect to the server)
## Internet Sockets

## Servers
bound to IP:port
### TCP
socket - opts - bind - listen - accept
accept: returns a socket for communication with that client only

### UDP
socket - opts - bind - send/recv

## Clients
randomly assigned port
### TCP
socket - opts - connect
### UDP


do spawned sockets each get their own port?


# Common errors - now understood
- mysql (unix domain sockets). ls -l will show it's a socket, not a normal file
"Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2) when trying to connect?"
- something about "error: [Errno 32] Broken pipe"

# Where is it used?
e.g. python's httplib establishes http connections using sockets, and is in turn used by urllib2.Request; requests library (popular 3rd party library) uses sockets to establish connections as well; look for `import socket`; urllib is in turn used by cherrypy (a small python web framework) and others

# Workshop
Alena Kuczynski, Rachel, Ye Eun, there were a couple guys I don't remember
said I will announce it start of next week

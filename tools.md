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

FIXME: telnet vs curl?

# Looking at where network sockets are created
./tcp-server.py  # start a server (alternative: with telnet/socat/something else? i.e., code-less)
on linux:
PID=`pgrep python`; ls -lh /proc/$PID  # will contain the socket file
on OSX:
lsof | awk '{print $5}' | sort | uniq  # show all currently present file types
lsof | grep IPv6  # will show our socket
since sockets are not "real" files, they are not shown by the OSX filesystem (?)
lsof stands for 'list open files', so it lists files (or file-like things) that currently exist, even though the file system might not show them

Same for unix sockets:
lsof -U (see man lsof for more socket options)

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

use "broken pipe" somewhere as an example

# inetd/launchd
My inetd-style launchd plist file for `/Users/margold/RC/networking/inetd-server.py` is in `~/Library/LaunchAgents/margold.inetd.server.plist`.
It can be launched with `launchctl load $path` and talked to with `telnet localhost 12345`
Documentation is here: https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html
Some more ideas are here: http://paul.annesley.cc/2012/09/mac-os-x-launchd-is-cool/

# Qs
write same server in a different language? Haskell? Probably for later this week, or the week after
looks like I need to understand pipes in order to understand stream sockets better
implement something small with sockets (chat client? there must be tutorials for this)

# Thursday
kernel networking security issues mini-talk?

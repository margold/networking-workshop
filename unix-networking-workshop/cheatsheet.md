# Exercise #1

- `lsof -ai -n`
- `netstat -np tcp` (on OSX)
- `netstat --inet -np` (on Linux)

---

# Exercise #1

```bash
# display all processes (`ax`) in a user-oriented format (`u`)
ps axu

# on Linux, `f` will display processes in an ASCII-art hierarchy tree
ps axuf
```

```bash
# lsof stands for "list open files"
# list all network sockets (-i) that firefox (-c) has open
# don't convert number addresses to host names (-n)
lsof -ai -n -c firefox
```

```bash
# on OSX:
# list all tcp connections (-p tcp)
# don't convert number addresses to host names (-n)
netstat -np tcp

# on Linux:
# list all internet connections (--inet)
# don't convert number addresses to host names (-n)
# show process ids (-p)
netstat --inet -np
```

---

# Exercise #2

- `ifconfig lo0`
- `ifconfig en0` or `ifconfig eth0`
- or just `ifconfig`

---

# Exercise #3

```bash
# run a simple HTTP server
# SimpleHTTPServer server comes built-in in Python
# choose any port you want, eg. 8000
python -m SimpleHTTPServer <port>
```

``` bash
# open an insecure (!) text-based connection
# to a server at host:port
telnet <host> <port>
```

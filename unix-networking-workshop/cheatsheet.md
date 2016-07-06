# Exercise #1

- `lsof -ai -n`
- `netstat -np tcp`

---

# Exercise #1

```bash
# lsof stands for "list open files"
# list all network sockets (-i) that firefox has open
# don't convert number addresses to host names (-n)
lsof -ai -n -c firefox
```

```bash
# list all tcp connections (-p tcp)
# don't convert number addresses to host names (-n)
netstat -np tcp
```

---

# Exercise #2

- `ifconfig`
=> FIXME add a bit more (maybe options)

---

# Exercise #3

```bash
# run a simple HTTP server
python -m SimpleHttpServer 8080
```
=> FIXME what does it mean that it's an http server? try sending http to it

``` bash
# open an insecure (!) text-based connection
# to a server at host:port
telnet <host> <port>
```

---

# Exercise #4

=> FIXME: github link for example tcp socket polite web server

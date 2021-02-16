## Level Goal ##

The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

## Commands you may need to solve this level ##

    ssh, telnet, nc, openssl, s_client, nmap
    
## Helpful Reading Material ##

    Port scanner on Wikipedia
    
## Solution ##

This level introduces us to nmap - a port scanning utility. We would like to know which ports are open to us from a range of port 31000 to 32000. To do this we run `nmap localhost -p 31000-32000`. This returns with:

```
Starting Nmap 7.40 ( https://nmap.org ) at 2021-02-16 03:04 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00028s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown
```

We can see that there are five open ports in the specified range. When we attempt to connect to each one with SSL, as shown in level 15, only port xx returns with a valid password of .


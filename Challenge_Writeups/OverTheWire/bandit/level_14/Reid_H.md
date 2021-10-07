## Level Goal ##

The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

## Commands you may need to solve this level ##

    ssh, telnet, nc, openssl, s_client, nmap
    
## Helpful Reading Material ##

    How the Internet works in 5 minutes (YouTube) (Not completely accurate, but good enough for beginners)
    IP Addresses
    IP Address on Wikipedia
    Localhost on Wikipedia
    Ports
    Port (computer networking) on Wikipedia
    
## Solution ## 

This level involves a simple use of netcat. We need to connect to the local machine on port 30000 and submit the password to bandit14. When we run `nc localhost 30000` when are left with a stdin prompt. We can enter 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e and the program returns back the password of BfMYroe26WYalil77FoDi9qh59eK5xNr.

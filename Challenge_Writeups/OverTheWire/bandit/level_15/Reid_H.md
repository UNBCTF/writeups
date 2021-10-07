## Level Goal ##

The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…

## Commands you may need to solve this level ## 

    ssh, telnet, nc, openssl, s_client, nmap
    
## Helpful Reading Material ## 

    Secure Socket Layer/Transport Layer Security on Wikipedia
    OpenSSL Cookbook - Testing with OpenSSL
    
## Solution ##

 All we need to do for level 15 is the same as level 14 except connect using openssl instead of nc. The syntax can be found through the 'OpenSSL Cookbook - Testing with OpenSSL' resource linked in the actual challenge page. We connect by running `openssl s_client -crlf -connect localhost:30001 -servername localhost`. Next, a lot of information about the connection will display on the screen and you will enter a stdin prompt. Just submit the password from level 14 and it'll return with the next password of cluFn7wTiGryunymYOu4RcffSxQluehd.

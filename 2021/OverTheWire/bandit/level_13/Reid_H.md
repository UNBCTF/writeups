## Level Goal ##

The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

## Commands you may need to solve this level ##

    ssh, telnet, nc, openssl, s_client, nmap

## Helpful Reading Material ##

    SSH/OpenSSH/Keys
    
## Solution ##

In this level, we are given a private RSA key to log directly into bandit level 14. All we need to do is copy the contents of the file to our own machine to file (maybe bandit14.private?), change the permission of the file using `chmod 600 bandit14.private`, and log in using `ssh -i bandit14.private bandit14@bandit.labs.overthewire.org -p 2220`. We must change the file permissions of the bandit14.private file because the default permissions of 644 are too accessible for private data such as an RSA key. Read up on linux file permissions [here](https://www.linux.com/training-tutorials/understanding-linux-file-permissions/).

When we log into bandit14, we can output the contents of the '/etc/bandit_pass/bandit14' file and recieve our password of 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e (even though we don't really need it as we're *already* inside bandit14).

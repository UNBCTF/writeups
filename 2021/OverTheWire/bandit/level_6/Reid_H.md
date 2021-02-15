## Level Goal ##

The password for the next level is stored somewhere on the server and has all of the following properties:

    owned by user bandit7
    owned by group bandit6
    33 bytes in size

## Commands you may need to solve this level ##

ls, cd, cat, file, du, find, grep

## Solution ##

We can find a file 33bytes in size, owned by bandit7 and group bandit 6 by running `find / -user bandit7 -group bandit6 -size 33c`. This reveals a single file that we have permission to view: '/var/lib/dpkg/info/bandit7.password'. This file contains a password ofHKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs .

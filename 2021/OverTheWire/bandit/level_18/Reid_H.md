## Level Goal ##

The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

## Commands you may need to solve this level ##

    ssh, ls, cat
    
## Solution ##

From the description, we know that .bashrc logs us out when we attempt to gain a bash shell. A work around is to use a different shell altogether. If we run `ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/sh`, this will log us in with a 'sh' shell instead of bash. It may look like a stdin prompt, but you're actually in a shell!. Just type `ls` to list out the home directory contents and `cat readme` to obtain the password of IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x.

I'm not sure if this is the intended solution to this problem, but if it works it works.

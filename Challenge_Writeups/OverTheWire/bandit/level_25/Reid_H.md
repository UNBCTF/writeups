## Level Goal ##

Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

## Commands you may need to solve this level ##

    ssh, cat, more, vi, ls, id, pwd

To begin, we can output the contents of the '/etc/passwd' file to determine what the default shell is for bandit26. We see that it is '/usr/bin/showtext', so let's take a look at it:

```
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```

From this, we know that the more command is being executed when we log into bandit26. From the manual page (type `man more` in your terminal) we know that more displays the contents of a file; and, if the file is larger than the display screen size, the more program continues to run. We can exploit this property of the 'more' command by resizing our terminal to be smaller than the output of the 'text.txt' file. When we log into bandit26 with the given SSH key, we get put in a running instance of the 'more' command. From the man page again, we can enter the vi text editor by pressing 'v'. Now we can make use of vi commands while logged in as bandit26. First, let's change our vi shell to be bash with `:set shell=/bin/bash`. Now we can run bash commands through the vi editor. Let's run `cat /etc/bandit_pass/bandit26` to get our password of 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z.

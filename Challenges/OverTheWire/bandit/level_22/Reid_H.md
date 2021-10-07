## Level Goal ##

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

## Commands you may need to solve this level ##

    cron, crontab, crontab(5) (use “man 5 crontab” to access this)
    
## Solution ##

This level is very similar to the last level. When we output the contents of the '/etc/cron.d/' directory, we can see a cron job labeled 'cronjob_bandit23'. Once again the job is running every minute and calling the shell script '/usr/bin/cronjob_bandit23.sh'. The contents of this shell script is:

```
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

As this script is run as the bandit23 user, we know the output of `whoami` is 'bandit23'. Reading through the rest of the script, we can see that it is copying the bandit23 password to a file in the '/tmp' directory that has the name of the md5 hash of the user id. When we run the same command as the script to get the 'mytarget' variable value: `echo I am user bandit23 | md5sum | cut -d ' ' -f 1`, we get a hash of '8ca319486bfbbc3663ea0fbe81326349'. Outputing the contents of '/tmp/8ca319486bfbbc3663ea0fbe81326349' gives us the password of jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n.

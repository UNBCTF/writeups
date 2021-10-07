## Level Goal ##

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

## Commands you may need to solve this level ##

    cron, crontab, crontab(5) (use “man 5 crontab” to access this)
    
## Solution ##

Same as the past two. When we output the contents of '/usr/bin/cronjob_bandit24.sh' we see this:

```
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```

This script is executing all files in the '/var/spool/bandit24' directory as the bandit24 user that belong to the bandit23 user (us). We can go to the '/var/spool/bandit24' directory and create our own shell script. All our shell script needs to do is output the bandit24 password to a location we are able to read as the bandit23 user. For example:

```
#!/bin/bash
cat /etc/pass/bandit24_pass > /tmp/bandit24_pass
```

After this script runs at the top of the current minute, or when you manually execute '/usr/bin/cronjob_bandit24.sh' if you're impatient, we can output the contents of the '/tmp/bandit24_pass' file and obtain the password of UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ.


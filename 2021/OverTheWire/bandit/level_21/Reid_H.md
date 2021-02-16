## Level Goal ##

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

## Commands you may need to solve this level ##

    cron, crontab, crontab(5) (use “man 5 crontab” to access this)
    
## Solution ##

 When we list out the contents of the '/etc/cron.d/' directory, we see that there is a cronjob labeled 'cronjob_bandit22'. If we run `cat cronjob_bandit22`, we see that this particular cronjob has the properties '* * * * *' meaning it runs every minute of every hour of every day of every month of every year; and, it runs the command `/usr/bin/cronjob_bandit22.sh &> /dev/null` as bandit22. Let's take a look at '/usr/bin/cronjob_bandit22.sh'. It contains:
 
 ```
 #!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
 ```
 
 We can see that the shell script is outputting the password to level 22 in a file named t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv in the '/tmp' directory. When we output the contents of this  file with `cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`, we get the password of Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI.

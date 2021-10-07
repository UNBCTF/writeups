## Level Goal ##

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

## Commands you may need to solve this level ##

    ssh, nc, cat, bash, screen, tmux, Unix ‘job control’ (bg, fg, jobs, &, CTRL-Z, …)
    
## Solution ##

This one can be tricky and requires a working knowledge of netcat. First we must open up a netcat listener on a port that is not already in use, let's say 30303. We can do this by running `nc -l -p 30303`. Next, we have to background this process by pressing CTL+Z, so we can do other things while it is running. Now we get our SUID binary to connect to the port we've opened: `./suconnect 30303`. When we go back to our other process running nc by pressing CTL+Z and entering `fg 1`, we can paste our current password in the stdin prompt. Now, we can background the process again with CTL+Z and go check on our 'suconnect' program by CTL+Z and `fg 2`. We get a message saying the password matches and that it is sending the next password. Since the process has finished, we only have one process left running, so we can just run `fg` to bring it up and retrieve our password of gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr.

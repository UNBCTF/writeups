## Level Goal ## 

To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

## Helpful Reading Material ##

    setuid on Wikipedia

## Solution ##

When we list out the contents of the bandit19 user's home directory, we see an executable named 'bandit20-do'. When we run the executable, it outputs:

```
Run a command as another user.
  Example: ./bandit20-do id
```

Considering the name is 'bandit20-do' we can assume whatever command we run will be run as bandit20. Let's output the password using `./bandit20-do cat /etc/bandit_pass/bandit20`, and we GbKksEFF4yrVs6il55v6gwY5aVje5f0j.

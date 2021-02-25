# Leviathan1

First, ssh into the server using leviathan1 as the user using the password
gained from leviathan0.

```
ssh leviathan1@overthewire.org
password: rioGegei8m
```

To find the password for leviathan2, we performed ```ls -la``` and found an
executable called ```check```. This program is owned by leviathan2, which means
it could be useful for determining info about that user.

Running ```./check``` produced a prompt asking for a password, so we went in
search of that.

We ran ```radare2 ./check``` to analyze its assembly. Running ```afl``` showed
us that there is a ```main()``` function. We then used ```pdf @main``` to see
the main function in assembly.

It was noticed that some strings were being moved into variables, notably the
string 'sex' being moved into a variable called 's2', while the others were
being put into seemingly generic variables. This piqued our interest, so we
tried using 'sex' as the password.

```
./check
password: sex
```

This produced the output ```$``` meaning we were in a shell. Running ```whoami```
told us that the shell was owned by leviathan2. We printed out its password
using

```
cat /etc/leviathan_pass/leviathan2
```

which gave us

        ```ougahZi8Ta```
# Leviathan1

First, ssh into the server using leviathan1 as the user using the password
gained from leviathan0.

```
ssh leviathan1@overthewire.org
password: rioGegei8m
```

To find the password for leviathan2, we performed ```ls -la``` and found an
executable called ```check```. This program is owned by leviathan2, which means
it could be useful for determining info about that user.

Running ```./check``` produced a prompt asking for a password, so we went in
search of that.

We ran ```radare2 ./check``` to analyze its assembly. Running ```afl``` showed
us that there is a ```main()``` function. We then used ```pdf @main``` to see
the main function in assembly.

It was noticed that some strings were being moved into variables, notably the
string 'sex' being moved into a variable called 's2', while the others were
being put into seemingly generic variables. This piqued our interest, so we
tried using 'sex' as the password.

```
./check
password: sex
```

This produced the output ```$``` meaning we were in a shell. Running ```whoami```
told us that the shell was owned by leviathan2. We printed out its password
using

```
cat /etc/leviathan_pass/leviathan2
```

which gave us

        ```ougahZi8Ta```

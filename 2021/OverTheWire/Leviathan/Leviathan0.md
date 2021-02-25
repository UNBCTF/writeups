# Leviathan0

This one was given to us, we just had to ssh into the leviathan server.

```
ssh leviathan0@leviathan.labs.overthewire.org -p 2223
pasword: leviathan0
```

To find the password for leviathan 1, perform ```ls -la``` on the home directory.
There is a ```.backup``` folder with a file named ```bookmarks.html```. Opening
this in ```vim``` and searching for "password" produced the key

        rioGegei8m

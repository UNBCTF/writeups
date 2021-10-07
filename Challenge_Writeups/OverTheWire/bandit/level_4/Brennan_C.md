# Level 4

ssh into the game using `ssh bandit4@bandit.labs.overthewire.org -p 2220` using the password
`pIwrPrtPN36QITSp3EQaw936yaFoFgAB`.

This one has the `inhere` directory again, but this time instead of a `.hidden` file we have 10 files named
`-file00` to `-file09`.

Using the `./` trick for files named `-` I used `file ./-fil00` to see that it is a `data` file. The data
inside this file is not human readable.

The `data` output means `file` failed to find out anything about the file.

So, I used `hexdump -C ./-file0[x] > /tmp/dump.txt && cat /tmp/dump.txt` to perform a hexdump of the file
and output it. I substituted the `[x]` for the different file numbers, 0 to 9. I found what looked like
a password in `./-file07` which was `koReBOKuIDDepwhWk7jZC0RTdopnAYKh`. The rest contained garbage.

I tried ssh-ing into bandit5 using this and it worked.

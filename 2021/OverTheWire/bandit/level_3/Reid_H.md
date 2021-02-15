## Level Goal ##

The password for the next level is stored in a hidden file in the inhere directory.

## Commands you may need to solve this level ##

ls, cd, cat, file, du, find

## Solution ##

First we must enter the 'inhere' directory with the command `cd inhere`. When attempting to list out the contents of the 'inhere' directory, it returns nothing. This is because the password is stored in what's called a 'hidden file'. Hidden files are prefixed with '.' and do not get output with the `ls` command unless you add the option of '-a' which means 'all'. The `ls -a` command reveals a file named '.hidden', and the `cat .hidden` command gives us the password - pIwrPrtPN36QITSp3EQaw936yaFoFgAB.

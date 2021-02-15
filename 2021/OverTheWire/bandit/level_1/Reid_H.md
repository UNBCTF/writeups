## Level Goal ##

  The password for the next level is stored in a file called - located in the home directory

## Commands you may need to solve this level ##

  ls, cd, cat, file, du, find

## Helpful Reading Material ##

  Google Search for “dashed filename”
  Advanced Bash-scripting Guide - Chapter 3 - Special Characters
  
## Solution ##

Since the cat command sees '-' as a synonym for stdin, we must tell the cat command that '-' is a file in the current directory. We do this by prefixing the '-' file with './'. This makes the successful command `cat ./-`.

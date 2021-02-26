## Level Info ##

Welcome to Krypton! The first level is easy. The following string encodes the password using Base64:

    S1JZUFRPTklTR1JFQVQ=

Use this password to log in to krypton.labs.overthewire.org with username krypton1 using SSH on port 2231. You can find the files for other levels in /krypton/

## Solution ##

From the format of the given string, I recognize it as a Base64 string. Let's run `echo 'S1JZUFRPTklTR1JFQVQ=' | base64 -d` in our terminal to recieve the level password of KRYPTONISGREAT.

## Level Goal ##

The password for the next level is stored in a file called spaces in this filename located in the home directory

## Commands you may need to solve this level ##

    ls, cd, cat, file, du, find

## Helpful Reading Material ##

    Google Search for “spaces in filename”

## Solution ##

When referencing a file with spaces in the name, bash requires us to utilize the escape character '\' to signify the next character should be interpreted as text instead of its regular use (in this case, a delimeter). Therefore the `cat spaces\ in\ this\ filename` command gives us the password of UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK.

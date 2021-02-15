## Level Goal ##

The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

## Commands you may need to solve this level ##

ls, cd, cat, file, du, find

## Solution ##

When listing out contents of the 'inhere' directory, we see 10 different files. From the level description we know that only one of them is human readable. We can check the file type of the first one by running `file ./-file00`. This tells us that the file is of type 'data', which is not human-readable. We can use a bash for loop to check the file type of all the files with a single command of `for i in {0..9}; do file ./-file0${i}; done`. This shows us the ./-file07 contains 'ASCII text' while the rest contain 'data'. We can then check the contents of ./-file07 giving us the password of koReBOKuIDDepwhWk7jZC0RTdopnAYKh.

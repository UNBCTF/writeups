## Level Goal ##

The password for the next level is stored in the file data.txt next to the word millionth

## Commands you may need to solve this level ##

    grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

## Solution ##

To find the next password, we can run the command `cat data.txt | grep millionth`. This command outputs the contents of data.txt to the input of the grep command. The grep command filters out all lines of the input that does not include the given word (millionth). The output of our command gives 'millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV', which is our password.

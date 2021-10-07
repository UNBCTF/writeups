## Level Goal ##

The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

## Commands you may need to solve this level ##

    grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv, file
    
## Helpful Reading Material ##

    Hex dump on Wikipedia

## Solution ##

This one takes a bit of time. You'll start off with a data.txt file which contains a hexdump. Start by reversing this hexdump into a binary file with `xxd -r data.txt > data.txt`. Now you can run `file data.txt` which will tell you the type of compression the file was compressed with. For gzip, you'll want to change the file to a '.gz' file. For tar, you'll want to change the file to a '.tar' file. For bzip2, you'll want to change the file to a '.bz2' file. You can use the `mv` command to change file names. You'll continue decompressing and changing file names until you are left with an ASCII text file containing the password of 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL.

Example of how to change a '.txt' file to a '.gz' file:

    mv data.txt data.gz
    
Example of how to decompress all three types of compressed files:

    gunzip data.gz
    tar -xf data.tar
    bzip2 -d data.bz2

## Level Goal ##

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

## Commands you may need to solve this level ## 

    grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

## Helpful Reading Material ## 

    Piping and Redirection
    
## Solution ##

We can find unique lines by sorting the data, then using the `uniq` command to output unique lines. We must first sort the data as uniq only operates on adjacent lines. The `sort data.txt | uniq -u` command gives us a password of UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR.

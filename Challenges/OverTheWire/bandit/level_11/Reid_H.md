## Level Goal ##

The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

## Commands you may need to solve this level ##

    grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
    
## Helpful Reading Material ##

    Rot13 on Wikipedia
    
## Solution ##

Since the level description tells us that the file has been rotated by 13 positions, we can rotate it back by running the following command: `cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'`. The 'tr' component of this command is a translation command, and it maps each letter to another letter through the two inputs shown. Through this command we get a password of 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu.

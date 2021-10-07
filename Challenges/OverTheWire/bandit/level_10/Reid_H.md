## Level Goal ## 

The password for the next level is stored in the file data.txt, which contains base64 encoded data

## Commands you may need to solve this level ##

    grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

## Helpful Reading Material ##

    Base64 on Wikipedia
    
## Solution ##

When we output the contents of data.txt, we see `VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==`. Through research or experience we know that this is a base64 encoded string. To decode, we can run `base64 -d data.txt`. This gives us our password of IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR.

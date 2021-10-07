## Level Info ##

The password for level 2 is in the file ‘krypton2’. It is ‘encrypted’ using a simple rotation. It is also in non-standard ciphertext format. When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries. This helps obfuscate any patterns. This file has kept the plain text word boundaries and carried them to the cipher text. Enjoy!

## Solution ##

Since we know that the ciphertext is found in a file named 'krypton2', let's run `find / f -name krypton2` to find all the files on the system with this name. In the ouput we see the file '/krypton/krypton1/krypton2'. The contents of this file are:

```
YRIRY GJB CNFFJBEQ EBGGRA
```

The level info has already told us that a simple rotation ecryption algorithm was used on the file. The most popular rotational algorithm is rot13, so let's see if it is using that. The output of the commmand `cat /krypton/krypton1/krypton2 | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'` is the password of LEVEL TWO PASSWORD ROTTEN.

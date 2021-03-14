# Problem 

given an ASCII file with a clearly-encrypted line of text.
The name of the file is `esab64`, clearly just `base` backwards.

#Solution

Reverse the contents of the file and run it through `base64 -d`
This returns the text `_}e61e711106bd0db1b78efa894b1125bf{galf`
Reversing this gives us `flag{fb5211b498afe87b1bd0db601117e16e}`



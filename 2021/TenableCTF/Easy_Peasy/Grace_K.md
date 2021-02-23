## Easy Peasy - 50 points ##
'''
NzMgNzkgNmUgNzQgN2IgNzAgNjIgNjEgNzQgNjUgNmUgNjcgNjYgNWYgNmMgNjIgNjggNWYgNzQgNjIgNjcgNWYgN2EgNzIgN2Q=
'''

## Solution ##

I assumed it was a base64 encoded string and (on linux command line) ran 'echo NzMgNzkgNmUgNzQgN2IgNzAgNjIgNjEgNzQgNjUgNmUgNjcgNjYgNWYgNmMgNjIgNjggNWYgNzQgNjIgNjcgNWYgN2EgNzIgN2Q= | base64 --decode', which gave '73 79 6e 74 7b 70 62 61 74 65 6e 67 66 5f 6c 62 68 5f 74 62 67 5f 7a 72 7d'.
We can do a hex to ASCII conversion of that by running 'echo 73 79 6e 74 7b 70 62 61 74 65 6e 67 66 5f 6c 62 68 5f 74 62 67 5f 7a 72 7d | xxd -p -r', which gives us 'synt{pbatengf_lbh_tbg_zr}'. (We could also use a hex to ASCII online converter such as https://www.rapidtables.com/convert/number/hex-to-ascii.html).
We can then try decrypting it back from ROT13 by running 'echo synt{pbatengf_lbh_tbg_zr} | tr '[A-Za-z]' '[N-ZA-Mn-za-m]''.  This gives us the flag:
'''
flag{congrats_you_got_me}
'''

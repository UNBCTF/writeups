We are given a JPG image to start. The description says 'This garden contains more than it seems.' which makes me immediatley think this is a stegonography challenge.

By downloading the file and running the `strings garden.jpg` in our terminal, we can see the all the ASCII strings encoded into this image. If we run `strings garden.jpg | grep -oE "picoCTF{.*}"`, we can filter the output to just show us the flag.

We can then submit the flag: picoCTF{more_than_m33ts_the_3y3657BaB2C}.

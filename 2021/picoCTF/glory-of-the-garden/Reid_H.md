We are given a JPG image to start. The description says 'This garden contains more than it seems.' which makes me immediatley think this is a stegonography challenge.

By downloading the file and running the `hexdump -C /path/to/file` in our terminal, we can see the flag's ascii characters that were encoded into the image.

![flag-image](https://i.imgur.com/vKuSxMK.png)

We can then submit the flag: picoCTF{more_than_m33ts_the_3y3657BaB2C}.

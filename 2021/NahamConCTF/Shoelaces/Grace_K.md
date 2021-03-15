## Shoelaces - 50 points ##
```
Do you double-knot your shoelaces? You gotta keep'em tied!

Download the file below.
```
*The shoelaces.jpg file is in the Shoelaces folder.*

## Solution ##

I ran the following command to see if there was a flag in the hexdump of the file: `xxd shoelaces.jpg | grep flag`.
It returned the line `00007850: 666c 6167 7b31 3337 3238 3865 3936 3061  flag{137288e960a`, so I ran `xxd shoelaces.jpg | grep --color flag -A 10` to get the rest of the flag: 
```
flag{137288e960a3ae9b148e8a7db16a69b0}

## Random Encryption ##

We found the following file on a hacked terminal:

```
import random
flag = "flag{n0t_that_r4ndom}"
seeds = []
for i in range(0,len(flag)):
    seeds.append(random.randint(0,10000))

res = []
for i in range(0, len(flag)):
    random.seed(seeds[i])
    rands = []
    for j in range(0,4):
        rands.append(random.randint(0,255))

    res.append(ord(flag[i]) ^ rands[i%4])
    del rands[i%4]
    print(str(rands))

print(res)
print(seeds)
```



We also found sample output from a previous run:

```
[22, 67, 142]
[57, 51, 53]
[97, 114, 14]
[16, 94, 107]
[187, 79, 172]
[138, 138, 118]
[32, 41, 8]
[93, 104, 248]
[112, 33, 215]
[22, 163, 8]
[170, 21, 156]
[183, 196, 255]
[62, 160, 64]
[93, 124, 68]
[53, 227, 187]
[234, 44, 74]
[96, 171, 138]
[161, 46, 45]
[186, 114, 154]
[188, 137, 120]
[239, 44, 13]
[209, 17, 111, 78, 180, 98, 205, 186, 202, 124, 139, 37, 57, 95, 47, 136, 114, 168, 139, 204, 165]
```

Can you decode it?

## Solution ##

Now. This took me a while. It took me so long because in the sample ouput they didn't include the seeds line even though the example code expicitly shows the line 'print(seeds)'. I thought it was intentional but the next morning they released the 'Random Encryption Fixed' challenge which included the line with the seeds (which makes this challenge a whole lot easier). I figured it out without the seed values after trying for over two hours. I'm not still mad, you are. /s

So basically this program works in 3 steps:

1. Generate a random number between 0 and 10000 for each character of the flag

2. For each character in the flag:

    a) seed the random number generator with the corresponding random number from step 1
    
    b) generate the first four random numbers in the sequence
    
    c) XOR the character code of the flag character with the (i%4)th number in the sequence generated from step b.
    
    d) Append the result of step c to the 'res' list
    
    e) delete the (i%4)th number in the sequence generated from step b
    
    f) print the sequence generated from step b (without the (i%4)th number)
    
3. Print out the 'res' list

We need to find a way to recover the flag that was used in generating the sample output. This program uses a psuedo-random number generator, so the numbers aren't actually random. If you're not familair with these, read up on them [here](https://www.geeksforgeeks.org/pseudo-random-number-generator-prng/) There's definitely more efficient ways to do this, but this is the route I went.

I used the following python program to generate the first four numbers in sequence for all seeds from 0-10000:

```
import random

for i in range (0,10000):
    random.seed(i)
    val1 = random.randint(0,255)
    val2 = random.randint(0,255)
    val3 = random.randint(0,255)
    val4 = random.randint(0,255)
    print("Seed %d: %d, %d, %d, %d"%(i,val1,val2,val3,val4))
```

I ran this program and directed the output to a text file with `python3 random_encryption_seed.py > seeds.txt`.

The output follows the following format from lines 0-10000:

```
Seed 0: 197, 215, 20, 132
Seed 1: 68, 32, 130, 60
Seed 2: 28, 46, 43, 184
Seed 3: 121, 66, 189, 242
Seed 4: 120, 155, 52, 202
Seed 5: 130, 183, 14, 238
Seed 6: 41, 248, 133, 18
Seed 7: 165, 77, 202, 24
Seed 8: 116, 189, 192, 64
Seed 9: 237, 191, 136, 70
...
```

Now we can manually go through each line of the sample output, keeping in mind which value is missing in the printed sequence from 'line#%4' with the first line being index 0. This means that the first line is missing the first value in the sequence, the second the second value, and the eleventh the fourth value and so on.

For the first line, I search for the sequence of '22, 67, 142' in my text editor and it finds the following line:

    Seed 9593: 183, 22, 67, 142
    
We can see that the missing number is 183. This is the number that was XOR'd with the first flag character code to give us the res[0] value of 209. Since the XOR operation if reversible, we can obtain the flag character code by doing the XOR of 209 and 183. Then, we can take that result and turn it into the corresponding flag character! I did this through a python interpreter by running `python3` like so:

```
>>> 209 ^ 183
102
>>> chr(102)
'f'
```

Sure enough, if we go through each line given in the sample output, we can peice together 'flag{n0t_so_r4ndom}'

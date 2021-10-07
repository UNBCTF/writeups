# Level 5

ssh into the game using `ssh bandit5@bandit.labs.overthewire.org -p 2220` using the password
`koReBOKuIDDepwhWk7jZC0RTdopnAYKh`.

This one has the `inhere` directory but it is full of 20 additional directories. Each one of these folders
contains the same files/executables.

The overthewire instructions say the file needs to be "human readable, be 1033 bytes an non-executable'.
I used `find -type f -size 1033c` to search for all files (-type f) with a size of 1033 bytes (c means byte)
This returned the file in `/maybehere07/.file2` which contained the text `DXjZPULLxYr17uwoI01bNLQbtFemEgo7`


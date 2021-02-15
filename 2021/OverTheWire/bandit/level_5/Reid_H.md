## Level Goal ##

The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

    human-readable
    1033 bytes in size
    not executable

## Commands you may need to solve this level ##

    ls, cd, cat, file, du, find
    
## Solution ##

 We can use the find command to search for a file with specific properties; we'll check for a file size of 1033 bytes. The `find /home/bandit5/inhere -size 1033c` recursivley checks the '/home/bandit5/inhere' directory for all files of size 1033 bytes. This outputs a single file: '/home/bandit5/inhere/maybehere07/.file2'. Viewing the contents of this file gives us a password of DXjZPULLxYr17uwoI01bNLQbtFemEgo7.

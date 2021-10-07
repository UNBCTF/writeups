## Level Goal ##

There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19

## Commands you may need to solve this level ##

    cat, grep, ls, diff
    
## Solution ##

When we log into level 17 using the RSA key found in level 16, we find two files. We know that the password is in passwords.new and is the only line that differentiates the two files. We can use `diff passwords.old passwords.new` to output the difference between the two files. This gives us a password of kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd.

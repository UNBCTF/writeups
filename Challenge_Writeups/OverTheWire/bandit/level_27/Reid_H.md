## Level Goal ##

There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo. The password for the user bandit27-git is the same as for the user bandit27.

Clone the repository and find the password for the next level.

## Commands you may need to solve this level ##
 
    git
    
## Solution ##

This level is pretty straight forward if you are familiar with git. First, we must navigate to a directory where we have write permissions such as '/tmp'. Next we run `git clone ssh://bandit27-git@localhost/home/bandit27-git/repo` and select 'yes' when it prompts you to continue connecting. Next we can navigate to the repo we just cloned with `cd repo`, read the README file with `cat README`, and get the password of 0ef186ac70e04ea33b4c1853d2526fa2.

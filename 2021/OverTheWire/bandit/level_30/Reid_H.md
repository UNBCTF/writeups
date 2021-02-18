## Level Goal ##

There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo. The password for the user bandit30-git is the same as for the user bandit30.

Clone the repository and find the password for the next level.

## Commands you may need to solve this level ##

    git
    
## Solution ##

Same steps as past levels to clone the repo. This took some trial and error but with enough research through the man page of the git command, I was able to learn about tagging. From what I understand, git allows you to group together different commits with a description using a 'tag'. When running `git tag`, you'll see a tag titled 'secret'. We can run `git show secret` to view the details of the tag, which ends out being the password of 47e603bb428404d265f59c42920d81e5.

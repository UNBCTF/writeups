## Level Goal ##

There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo. The password for the user bandit30-git is the same as for the user bandit30.

Clone the repository and find the password for the next level.

## Commands you may need to solve this level ##

    git
    
## Solution ##

Same as previous levels for cloning the repo. The contents of the 'README.md' file say that we just need to push a certain file with certain contents to the origin. To do so, let's create the file with `echo 'May I come in?' > key.txt`. When we try to stage the file with `git add .`, we get a warning telling us that our path is listed in a .gitignore file. Let's override this by running `git add -f .`, commit our changes with `git commit -m "Hopefully this works..."` and push to the origin with `git push -u origin`. Now it'll return us this message with the password in the middle:

```
remote: ### Attempting to validate files... ####
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
remote: Well done! Here is the password for the next level:
remote: 56a9bf19c63d650ce78e6ec0354ee45e
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
```

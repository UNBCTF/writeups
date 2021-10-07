## Level Goal ##

There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo. The password for the user bandit28-git is the same as for the user bandit28.

Clone the repository and find the password for the next level.

## Commands you may need to solve this level ##

    git
    
Following the same steps from the last two levels, we first need to clone the repo. Next, we can check the contents of the README.md file.

```
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>
```

The "no passwords in production" makes me think there must be a developement branch somewhere with the credentials. When we check `git branch`, only 'master' comes up. This is because `git branch` only shows us local branches, not remote branches. Let's check the remote branches with `git branch -r`.

```
  origin/HEAD -> origin/master
  origin/dev
  origin/master
  origin/sploits-dev
```

We can see that there *is* a development branch. Let's switch to it with `git checkout origin/dev`, output the contents of 'README.md', and retrieve the password of 5b90576bedb2cc04c86a9e924ce42faf

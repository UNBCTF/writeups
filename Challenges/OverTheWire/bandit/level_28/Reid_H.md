## Level Goal ##

There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo. The password for the user bandit28-git is the same as for the user bandit28.

Clone the repository and find the password for the next level.

## Commands you may need to solve this level ##

    git
    
## Solution ##

This level is similar to level 28, however we cannot make another reposity with the name 'repo' and we cannot modify items in the '/tmp' directory. We can add another parameter to the cloning command which effectivley renames the local repository (`git clone ssh://bandit28-git@localhost/home/bandit28-git/repo repo2`). After we clone the repository, we see the 'README.md' file contains:

```
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
```

After a fair bit of attemping different git commands, trying `git log` seemed to give us useful information. 

```
commit edd935d60906b33f0619605abd1689808ccdd5ee
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    fix info leak

commit c086d11a00c0648d095d04c089786efef5e01264
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    add missing data

commit de2ebe2d5fd1598cd547f4d56247e053be3fdc38
Author: Ben Dover <noone@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    initial commit of README.md
```

From the logged changes to the repo we see that the password was previously in the README.md file. Let's use `git log -p | less` to view the changes that each commit introduced.

```
commit edd935d60906b33f0619605abd1689808ccdd5ee
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    fix info leak

diff --git a/README.md b/README.md
index 3f7cee8..5c6457b 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: bbc96594b4e001778eee9975372716b2
+- password: xxxxxxxxxx
```

We can see in this commit that the password of bbc96594b4e001778eee9975372716b2 was removed.

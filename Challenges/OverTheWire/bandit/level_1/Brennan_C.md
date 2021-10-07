# Level 1

ssh into the game using `ssh bandit1@bandit.labs.overthewire.org -p 2220` using the password
`boJ9jbbUNNfktd78OOpsqOltutMc3MY1`.

There is a file named `-` which doesn't produce any output from `file`, `cat` or `vim`. It turns out
this is because a file name of `-` is special. As an argument it refers to stdin or stdout. In order to
open it you need to provide the path. Running `cat ./-` gave the password `CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9`.

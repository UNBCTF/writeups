# leviathan2

As usual, ssh into the leviathan server using leviathan2 as the user.

```
ssh leviathan2@leviathan.labs.overthewire.org -p 2223
password: ougahZi8Ta
```

To find the password for leviathan3, we started by searching all the files.
```ls -la``` showed us an executable called ```printfile``` which is owned
by leviathan3. Looking at the assembly in the same way as leviathan2 we
saw that the program takes in user input but does not restrict it in any way.
We tried getting it to print the contents of custom files:

```
//the tmp directory allows write access for this purpose
echo 'hello' > /tmp/test.txt
./printfile /tmp/test.txt
```
Which worked! We got the output ```hello```.

this led us to try executing a custom command through the program, thinking
leviathan3 would execute it since it owned the program. This is where we hit
a roadblock because the additional command we provided through a pipe was
being executed by leviathan2 instead of leviathan3 like we hoped.

### We ended the meeting here

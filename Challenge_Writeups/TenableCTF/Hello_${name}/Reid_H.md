## Hello ${name} ##

Read a string from stdin using C/C++. This string is a person's name. Please greet them politely by printing "Hello ${Name}" to stdout.

stdin example:

    John
    
stdout example:

    Hello John
    
Ensure not to print anything else besides your answer during your code execution!*

## Solution ##

I know my code for this challenge is vulnerable to buffer overflow ... but it gets the points.

```
#include <stdio.h>
int main()
{
   char buf[20];
   scanf("%s",buf);
   printf("Hello %s", buf);
   return 0;
}
```

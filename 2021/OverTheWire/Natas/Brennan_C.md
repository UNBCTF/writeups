# Level 0

Go to http://natas0.natas.labs.overthewire.org and login with `natas0` as both username and password.

Open the inspector and open the div with id "content". The password for natas1 is listed there as a comment.

`gtVrDuiDfck831PqWsLEZy5gyDz1clto`

# Level 1

Go to http://natas1.natas.labs.overthewire.org. Username: `natas1`, password shown above.

View the page source and see the password on the bottom.

`ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi`

# Level 2

Go to http://natas2.natas.labs.overthewire.org/. Username: `natas2`.

There is a .png file located at /files/pixel.png. It is a single white pixel.

We know that /files is a valid directory, so navigating to it we see a users.txt file.

```
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
eve:zo4mJWyNj2
mallory:9urtcpzBmH
```

# Level 3

http://natas3.natas.labs.overthewire.org. Username: natas3

Look in robots.txt and see that s3cr3t is a disallowed directory. That means it isn't shown, but still
accessible. Go to that directory, click on users.txt and get the natas4 password.

`Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ`

# Level 4

You have to use a tool like burpsuite for this. Kali has it installed already. 

In Firefox, open preferences, scroll to the bottom, open network settings. Choose Manual proxy configuration
and set the HTTP Proxy to be 127.0.0.1 at port 8080.

Run burbsuite using

```
$ burpsuite
```

Create a temporary project (click next), use Burp defaults, and go to the proxy tab. 
Within the proxy page there is an intercept tab, make sure "intercept is on" is shown.

Go to the natas4 page and click the "refresh page" button.

Burpsuite will show you the raw request, containing a "Referer". Change the value of the referer to be
http://natas5.natas.labs.overthewire.org/ to trick the website into thinking that's where you're coming
from.

Click the "forward" button to send the modified data along, then look at the natas4 page to get the password
for natas5.

`iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq`

Make sure to go back into the preferences->network settings and change the proxy setting back to what it was.

# Level 5

http://natas5.natas.labs.overthewire.org/. Username natas5

The welcome message is "Access disallowed. You are not logged in". This sounds like a cookies thing, so
open the storage tab of the developer tools and look at the cookies.

Set the value of "loggedin" to 1 and refresh the page.

`aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1`

# Level 6

http://natas6.natas.labs.overthewire.org


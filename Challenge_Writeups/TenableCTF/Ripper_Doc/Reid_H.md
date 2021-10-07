## Ripper Doc ##

    Find the flag in the ripper doc list.

    http://167.71.246.232/

    Alternate: http://167.71.246.232:8080/

## Solution ##

When we visit the webpage given, we see the following screen:

![webpage](https://i.imgur.com/QGEztXq.png)

We can see a link to a page titled 'Certified Ripper Docs', so let's take a look.

![ripper-docs](https://i.imgur.com/2Gg44PE.png)

Hmmm. It looks like we're not authenticated and can't view this page. It is interesting how there are no login options but the site requires authentication. Let's check the cookies in the browser's development console.

![dev-console](https://i.imgur.com/tMjo1Ti.png)

There's an 'authenticated' cookie with a value of 'false'. Let's just double-click on it, change it to 'true' and refresh the page.

![ripper-docs-authenticated](https://i.imgur.com/QFGW3Ip.png)

There it is! flag{messing_with_cookies}

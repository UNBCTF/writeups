
https://google-gruyere.appspot.com/#0__hackers  
https://google-gruyere.appspot.com/529298633727819305970592574332893494382/

# About the code

gruyere.py: Main web server  
data.py: Stores default data in the database  
	- an admin and two default users  
gtl.py: Gruyere template language  
sanitize.py: module used for sanitizing html  
resources/... holds all template files, images, CSS, etc.  

# My Credentials

username: test  
password: test  

# Uploading files and creating snippets

Fill out account profile, then create a snipped via "New Snippet", upload a file via "upload".

# URL XSS

#### URL
https://google-gruyere.appspot.com/part2

#### Attempt

Use `%3C` for `<` and `%3E` for `>`

`https://www.google.com/search?q=flowers+%3Cscript%3Eevil_script()%3C/script%3E` is
then rendered as `flowers<script>evil_script()</script>` and `evil_script()` is run.

Use `alert(1)` as a test javascript script to see if there is a vulnerability.

For example: `https://google-gruyere.appspot.com/id/%3Cscript%3Ealert(1)%3C/script%3E`
causes an alert to appear with `1` as the message. (Replace id with your actual id)

# File Upload XSS

#### URL

https://google-gruyere.appspot.com/part2

#### Attempt

It is possible to run the code in an .html file in this website. You have the means to upload a file
and then open that file in a browser. When the file is opened whatever code inside it will be executed.

xss_script.html:
```
<script>
	alert(1)
</script>
```

Create an account in Gruyere (use credentials like Test,Test) and click on the upload link.

Choose the .html file and go to the URL the site gives you. When the page loads the code will
execute, resulting in an alert appearing with `1` as the text. If no message shows up you probably have
a browser add-on preventing pop-ups.

Congrats, you've successfuly performed a cross-site scripting attack.

An example link using my id:  
https://google-gruyere.appspot.com/529298633727819305970592574332893494382/test/xss_script.html

# Reflected XSS

#### URL

https://google-gruyere.appspot.com/part2

#### Attempt

## Headers for your Inspiration ##

    Find the flag here: http://167.71.246.232/

    Alternate: http://167.71.246.232:8080/

## Solution ##

Considering this is website is communicating over HTTP, we can assume the use of the word 'headers' in the challenge description is refering to HTTP headers.

Let's use cURL to make a request to the service and check the headers. To do this we run `curl -v http://167.71.246.232/`, with the '-v' meaning verbose mode.
From this we get the following output:

```
*   Trying 167.71.246.232:80...
* Connected to 167.71.246.232 (167.71.246.232) port 80 (#0)
> GET / HTTP/1.1
> Host: 167.71.246.232
> User-Agent: curl/7.75.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Mon, 22 Feb 2021 02:31:37 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Strict-Transport-Security: max-age=63072000; includeSubdomains
< X-Frame-Options: DENY
< X-Content-Type-Options: nosniff
< Flag: flag{headersftw}
< Vary: Accept-Encoding
< Content-Length: 1041
< Content-Type: text/html; charset=UTF-8
< 
```

We can see there is a 'Flag' header with the value of flag{headersftw}!

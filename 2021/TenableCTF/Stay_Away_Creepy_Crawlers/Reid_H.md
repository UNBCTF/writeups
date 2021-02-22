## Stay Away Creepy Crawlers ##

    Find the flag where they keep the creepy crawlers away.

    http://167.71.246.232/

    Alternate: http://167.71.246.232:8080/
    
## Solution ##

Considering this is in the 'Web App' category and it references 'crawlers', I immediately think to check the website's 'robots.txt' file. This is a special file that almost all websites have that gives direction to search engine crawlers that scrape all websites to index them. A better explanation can be found [here](https://www.sajari.com/blog/what-are-search-engine-crawlers).

When we route to http://167.71.246.232/robots.txt, we find the flag of flag{mr_roboto}.

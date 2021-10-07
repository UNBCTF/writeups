## Level Goal ## 

The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

## Commands you may need to solve this level ##

    grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
    
## Solution ##

Since running grep on binary files does not always work as intended, we can use the `strings` command to output all ASCII strings that are found in the specified file. With that output we can run grep to filter the output for lines that include a couple '=' characters. Running `strings data.txt | grep ======` gives us:

```
========== the*2i"4
========== password
Z)========== is
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```

And we can see our password in the last line.

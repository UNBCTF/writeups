## Very secure website - 200 points
### Category: Web

Some students have built their most secure website ever. Can you spot their mistake?

http://dctf1-chall-very-secure-site.westeurope.azurecontainer.io/


## Solution
The website provides the [source code](http://dctf1-chall-very-secure-site.westeurope.azurecontainer.io/source.php):
```
<?php
    if (isset($_GET['username']) and isset($_GET['password'])) {
        if (hash("tiger128,4", $_GET['username']) != "51c3f5f5d8a8830bc5d8b7ebcb5717df") {
            echo "Invalid username";
        }
        else if (hash("tiger128,4", $_GET['password']) == "0e132798983807237937411964085731") {
            $flag = fopen("flag.txt", "r") or die("Cannot open file");
            echo fread($flag, filesize("flag.txt"));
            fclose($flag);
        }
        else {
            echo "Try harder";
        }
    }
    else {
        echo "Invalid parameters";
    }
?>
```

From the source code we can see that the username and password are Tiger128,4 hash values.
[This website](https://md5hashing.net/hash/tiger128,4) decrypts the username hash value of `51c3f5f5d8a8830bc5d8b7ebcb5717df` to `admin`.
It is unable to decrypt the password hash value of `0e132798983807237937411964085731`.

[This website](https://www.whitehatsec.com/blog/magic-hashes/) explains that password hashes in PHP starting with 0e have "magic numbers".  The magic number for Tiger128,4 is `479763000`.

Using the decrypted username and the "magic number" as the password, we can log in and get the flag `dctf{It's_magic._I_ain't_gotta_explain_shit.}`.

# Strong Password

This one gives us a .zip file with a password protected file inside. I ran the following commands
in kali to get the password

`sudo gunzip /usr/share/wordlists/rockyou.txt`
`wc -l /usr/share/wordlists/rockyou.txt`
`zip2john strong_password.zip > strong_password.txt`
`john --wordlist=/usr/share/wordlists/rockyou.txt strong_password.txt`

Wait for it to finish...

`john --show strong_password.txt`

This gave me `Bo38AkRcE600X8DbK3600` as the password. Attempting to open the `lorem_ipsum.txt`
file with this password was successful.

Searching through the file for `dctf` I found the flag: `dctf{r0cKyoU_f0r_tHe_w1n}`

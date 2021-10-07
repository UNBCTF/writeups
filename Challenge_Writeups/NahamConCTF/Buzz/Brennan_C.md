# Problem

given a file called `buzz`. Running it through `file` gives `compress'd data 16 bits`

# Solution

This file type usually means Unix compression, so give the file the extension `.z`
Uncompress the file using `uncompress buzz.z`
This turns it into an ASCII file. `cat buzz.z` gives `flag{b3a33db7ba04c4c9052ea06d9ff17869}`


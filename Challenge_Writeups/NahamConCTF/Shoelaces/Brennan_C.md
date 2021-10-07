# Problem

Given a jpg, probably a stego problem

# Solution

Did a hexdump of the problem and grepped for `flag{`
The flag was found at x7850 and is `flag{137288e960a3ae9b148e8a7db16a69b0}`

# Commands

`xxd shoelaces.jpg | grep flag{`
`xxd shoelaces.jpg > output.txt && vim output.txt` Then `\ flag{`

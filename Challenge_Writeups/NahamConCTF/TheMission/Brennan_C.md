# The Mission

A linear, story-like challenge. Each solution leads to the next

# 1 - The Mission

The first part was checking out the description/rules for The Mission challenge. Using
the inspect tool on the page I found a comment which thanked me for reading the rules and
gave me the flag.

Page: https://ctf.nahamcon.com/mission
Flag: `flag{48e117a1464c3202714dc9a350533a59}`

Submitting this flag opens a new challenge called Bionic

# 2 - Bionic

We are given a link to a page for a company called `Constellations`: https://constellations.page/
Using the same inspect trick I found a comment: 
`Vela, can we please stop sharing our version control software out on the public internet?`

They provided links to social media accounts at the bottom, and I found `flag{e483bffafbb0db5eabc121846b455bc7}`
on their Twitter page. However, we are told that the key to Bionic is on the Constellation page, so this must
be for later.

Running `nmap -A -v constellations.page` I see that there is a tcp connection open on port 443 which
has git information. The comment I found mentioned version control, so maybe this is it. It says
there is a git repository at `34.117.193.93:443/.git/`. That ip is the constellations.page site.

The nmap output also says the repository is unmaed and to edit the file 'description' to name it.
The last commit message is: "Management said I need to remove the team details so I redac..."
It says the supported methods are GET HEAD POST and OPTIONS, so maybe a curl request is in order.

The nmap output also showed us that there is a page called `constellations.page/meet-the-team.html`
which we can't get to just by navigating the site. Going to this endpoint gives us the same page but
with the words: 
"Redacted Sorry, for security reasons our team has decided to no longer publicize employee names and info.". 

I got a brainwave and tried putting `/#flag` in the url to see if anything came out. Nothing.

Hell yeah, the flag was in constellations.page/robots.txt. The nmap output had it listed with 
"1 disallowed entry" so I put it in the url just for kicks. I should have checked that sooner.

`flag{33b5240485dda77430d3de22996297a1}`

# 3 - Meet The Team

I need to find the list of team members that was redacted as mentioned in part 2. I am looking for
a publicly available version control software folder published on the website itself.

There is a /.git/ endpoint but we don't have permission to access it. Maybe that can be changed?

Progress! The nmap output showed that there was a /.git/config file available, so adding that to the
url gave me some good info. 

```
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[user]
	name = Leo Rison
	email = leo.rison@constellations.page
```
Now I know there is a user named Leo Rison. Cool.

I googled where the commit messages are stored. This led me to add `COMMIT_EDITMSG` to the url, giving
me `constellations.page/.git/COMMIT_EDITMSG` and  the last commit message.
```
Management said I need to remove the team details so I redacted that page and added it to robots.txt
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# HEAD detached from 1142cc3
# Changes to be committed:
#	modified:   meet-the-team.html
#	new file:   robots.txt
#

```
Googling .git's file structure I learned that in addition to the /config there is also /index. Going to
`constellations.page/.git/index` prompted a download of a git index file.

There is also /HEAD which prints out this text: `e7d4663ac6b436f95684c8bfc428cef0d7731455`. This is not 
the flag though, this is a pointer to the HEAD of the current git branch.


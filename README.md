# HtB-Auto-Script

Since the pre-prep work for HtB is always the same, I created HAS to automate this task.

# Features

- Creates a Folder in a given ```PATH``` with the ```BOXNAME```.  
	-> Checks if the Folder already exist (If yes, skips the creation).
- Creates a ```"nmap"``` Folder in the ```BOXNAME```'s Folder.
- Adds the IP to ```"/etc/hosts"``` with ```BOXNAME``` and ```BOXNAME.htb```.
- Checks if you are connected to the HTB VPN.  
	-> if not loops till you are.
- Checks if ```BOXNAME``` is reachable.   
	-> loops till it is.  
	--> After 3 failed Pings, ask the User to continue or skip the Ping Check. 
- Opens your default Browser with the ```BOXNAME URL``` (~90% of HTB Machines have a Web server running).
- Copies the Pre-defined Folder with .md files into Obsidian.
- Copies the tmux files (.nice.py) in the ```BOXNAME```'s Folder.   
	--> I had to do this for the functioalty for the "Create new Panel" in tmux, and you're still in ```BOXNAME``` PATH.
- After 3 seconds opens tmux with 4 Panes:  
```nmap -sC -sV, gobuster or feroxbuster, ffuf for subdomain Enumeration, sleep 60; nmap -p- and if you like autorecon.```

# Installation

Firstly download HAS and move into the Foder:

```
git clone https://github.com/Clipsec/HtB-Auto-Script 

cd HtB-Auto-Script
```

Now you have to change a few things in the script (give it the right ```PATH```).

Have a closer look at:

- Folder Structure
- Obsidian Copy
- Tmux

after that you are ready to go!

```
python3 HAS.py
```

# Preview

![HAS](https://user-images.githubusercontent.com/32893797/175528655-1d1543ac-1870-4a6f-98b7-933f7a74dbcf.PNG)

# ToDo / Add soonish

- export ```BOXNAME``` as ```$target```.

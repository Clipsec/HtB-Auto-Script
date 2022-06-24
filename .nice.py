import pathlib
import os
from sys import argv
from os import system

# -----------------------------------------------------------
# Env
# -----------------------------------------------------------
path = pathlib.PurePath(os.getcwd())
BoxName = path.name.lower()
# -----------------------------------------------------------

# -----------------------------------------------------------
# How to do your own tmux Panel
# -----------------------------------------------------------
#  All you have to do it copy this:
#
#  tmux('new-window')
#  tmux('select-pane -t 2')
#  tmux_shell(' YOUR CODE OR TOOL COMMANd ')
#  tmux('rename-window "ffuf"')
#
#  and add "BoxName" for the BOXNAME.htb URL in the tool or command you wish to use. Easy as that
# -----------------------------------------------------------

def tmux(command):
    system('tmux %s' % command)

def tmux_shell(command):
    tmux('send-keys "%s" "C-m"' % command)

# New tmux session with the name "htb"
tmux('new-session -d -s htb')

# tmux Panel 1 namp
tmux('select-window -t 0')
tmux_shell('nmap -sC -sV -oA nmap/output ' + BoxName + '.htb')
tmux('rename-window "nmap"')

# tmux Panel 2 gobuster or ferosbuster
tmux('new-window')
tmux('select-pane -t 1')
tmux_shell('gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -u http://' + BoxName + '.htb -t 100 -x .php')
tmux('rename-window "gobuster"')
# Uncomment 
#tmux_shell('feroxbuster -u http://' + BoxName + '.htb -r -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 100 -x php') 
#tmux('rename-window "feroxbuster"')

# tmux Panel 3 ffuf
tmux('new-window')
tmux('select-pane -t 2')
tmux_shell('ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -u http://' + BoxName + '.htb -H "Host: FUZZ.' + BoxName + '.htb" -fw 20')
tmux('rename-window "ffuf"')

# tmux Panel 4 namp all Ports
tmux('new-window')
tmux('select-window -t 3')
tmux_shell('sleep 60; nmap -p- ' + BoxName + '.htb')
tmux('rename-window "nmap-AllPorts"')

# tmux Panel 5 autorecon
#tmux('new-window')
#tmux('select-pane -t 4')
#tmux_shell('autorecon ' + BoxName + '.htb')
#tmux('rename-window "autorecon"')

# Switch back to Panel 1
tmux('select-window -t 0')
tmux('a')

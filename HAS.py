import os
import pathlib
from sys import argv
import colorama
from colorama import Fore
import shutil
import time
import subprocess
import platform
import webbrowser

# Bold or not
fett = '\033[1m'
fettend = '\033[0m'

# -----------------------------------------------------------
# Folder Structure
# -----------------------------------------------------------

def folder_structure():
    print()
    print("----------------------------")
    print("# " + fett + Fore.CYAN + "Directory Path are made." + fettend, Fore.WHITE + "#")
    print("----------------------------")

    """Input from CLI for the Box-Name"""
    global BoxName
    BoxName = input("Box Name is: ")

    """Path for /Documents/HTB/Boxen/"""
    parent_dir = "/root/Documents/HTB/Boxen/" #CHANGE THIS to your PATH where you have your Documentation for the HTB Boxes
    global path
    path = os.path.join(parent_dir, BoxName)
    path2 = os.path.join(parent_dir, BoxName, "nmap")

    """Check for existing Folder"""
    if not os.path.exists(path):
        """Create Folder with BoxName in Path"""
        os.mkdir(path)
        print("-> Directory", fett + Fore.GREEN + BoxName + fettend, Fore.WHITE+"Created")

        """Create nmap Folder in BoxName-Folder"""
        os.mkdir(path2)
        print("-> Directory", fett + Fore.GREEN + "nmap" + fettend, Fore.WHITE + "in", fett + Fore.GREEN + BoxName + fettend, Fore.WHITE + "Created")
    else:    
        print(fett + Fore.RED + "-> Directory " + fett + Fore.GREEN + BoxName + Fore.RED + " already exists!!!", fettend)
folder_structure()

# -----------------------------------------------------------
# IP ADD
# -----------------------------------------------------------

def add_ip():
    print()
    print("-----------------------------")
    print("# " + fett + Fore.CYAN + "Add IP to /etc/hosts now." + fettend, Fore.WHITE + "#")
    print("-----------------------------")

    """Input for IP in /etc/hosts"""
    pathIP = "/etc/hosts"
    IPHtB = input("The IP is the following: ")

    """If needed another Name for the Box uncomment this"""
    #IPName = input("The Name to the Box: ")
    global IPName
    IPName = BoxName.lower()

    with open(pathIP, "a") as f:
      f.write("\n")
      f.write(IPHtB + "\t" + IPName + " " + IPName+".htb")

    print("-> The IP", fett + Fore.GREEN + IPHtB + fettend + Fore.WHITE + " was added to /etc/hosts with the Name to Resolve:", fett + Fore.GREEN + IPName + fettend + Fore.WHITE + " &", fett + Fore.GREEN + IPName + ".htb" + fettend + Fore.WHITE)
add_ip()

# -----------------------------------------------------------
# VPN Check
# -----------------------------------------------------------

def tun_checker():

    print()
    print("-------------------------------------------------------")
    print("# " + fett + Fore.CYAN + "Checking if you are connected to HTB via VPN (tun0)" + fettend, Fore.WHITE + "#")
    print("-------------------------------------------------------")

    while True:
        cmdout = subprocess.Popen(["ifconfig | grep tun"],stdout = subprocess.PIPE, shell=True).communicate()[0]
        time.sleep(1)
        if "tun".encode() in cmdout:
            print(fett + Fore.GREEN + "tun0" + fettend, Fore.WHITE + "is up and running." + fett + Fore.CYAN + " Moving on!" + fettend, Fore.WHITE)
            return
        if not "tun".encode() in cmdout:
            print(fett + Fore.GREEN + "tun0" + fettend, Fore.WHITE + "is" + fett + Fore.RED + " DOWN!" + fettend, Fore.WHITE)
tun_checker()

# -----------------------------------------------------------
# Ping Check
# -----------------------------------------------------------

def ping_check(site=IPName):
    
    hostname = IPName + ".htb"
    count = 0

    print()
    print("------------------------------------------")
    print("# " + fett + Fore.CYAN + "Checking if the Box is up and running." + fettend, Fore.WHITE + "#")
    print("------------------------------------------")

    # Windows or Linux
    param = '-n' if platform.system().lower()=='windows' else '-c'

    while True:
        status = subprocess.run(['ping', param, '3', hostname], capture_output=True)
        if status.returncode == 0:
            print(fett + Fore.GREEN + hostname + fettend, Fore.WHITE + "is up and running." + fett + Fore.CYAN + " Moving on!" + fettend, Fore.WHITE)
            return
        elif status.returncode == 1:
            print(fett + Fore.GREEN + hostname + fettend, Fore.WHITE + "is" + fett + Fore.RED + " DOWN! Repeating till " + Fore.GREEN + hostname + Fore.RED + " is up!" + fettend, Fore.WHITE)
            count +=1
            time.sleep(0)
            if count > 2:
                print()
                print("Maybe " + fett + Fore.GREEN + hostname + fettend, Fore.WHITE + " is not responding to Ping.")
                print("You wanna skip the Ping Check?")
                print("------------------------")
                print("--> If" + fett + Fore.GREEN + " Yes" + fettend, Fore.WHITE + ": Continue with the script.")
                print("--> If" + fett + Fore.RED + " No " + fettend, Fore.WHITE + ": We try another 3 times to Ping and ask again.")
                i = input("Y(es) or N(o)? : (Y/y N/n) ").lower()
                print()
                if i == "y":
                    break
                if i == "n":
                    count = 0
ping_check()

# -----------------------------------------------------------
# Open Browser
# -----------------------------------------------------------

def browser_open(BoxName):
    print()
    print("-----------------------------")
    print("# " + fett + Fore.CYAN + "Open the Box URL for you!" + fettend, Fore.WHITE + "#")
    print("-----------------------------")

    webbrowser.open(IPName + ".htb")
    print("-> Opend your Browser!")
browser_open(BoxName)

# -----------------------------------------------------------
# Obsidian Copy
# -----------------------------------------------------------

def obsidan_copy(BoxName):

    obsidian_parent_dir = "/root/Documents/Obsidian/HtB/" #CHANGE THIS to your PATH where you have your Documentation for the HTB Boxes
    obsidian_path = os.path.join(obsidian_parent_dir, BoxName)

    print()
    print("---------------------------------")
    print("# " + fett + Fore.CYAN + "Creating Folders for Obsidian" + fettend, Fore.WHITE + "#")
    print("---------------------------------")

    """Check for existing Folder"""
    if not os.path.exists(obsidian_path):
        """My Src Folder for Obsidan with all needed pre-configured .md files inside"""
        src = r"/root/Documents/Notes/NEWBOX" #CHANGE THIS to your PATH where you have stored your "Default" Folder for Obsidian
        dst = r"/root/Documents/Obsidian/HtB/NEWBOX" #CHANGE THIS to your PATH where you have your Documentation for the HTB Boxes
        shutil.copytree(src, dst)
        os.rename(r"/root/Documents/Obsidian/HtB/NEWBOX", r"/root/Documents/Obsidian/HtB/" + BoxName)
        print("-> Entry for Obsidian under HTB was made with: " + fett + Fore.GREEN + BoxName + fettend + Fore.WHITE + " ")
    else:    
        print(fett + Fore.RED + "-> Obsidian Directory " + fett + Fore.GREEN + BoxName + Fore.RED + " already exists!!!", fettend)
obsidan_copy(BoxName)

# -----------------------------------------------------------
# Tmux
# -----------------------------------------------------------

def tmux_create(BoxName, path):
    print()
    print("------------------------------------")
    print("# " + fett + Fore.CYAN + "Opening Tmux with Session as HtB" + fettend, Fore.WHITE + "#")
    print("------------------------------------")

    """Src of my .nice.py File"""
    src = r"/root/Documents/.nice.py" #CHANGE THIS to your PATH where you have this file stored
    shutil.copy(src, path)

    print("-> Waiting 3 sec.")
    time.sleep(1)
    print("-> Tmux start!")
    time.sleep(1)
    print()
    print("--> GO! <--")
    time.sleep(1)

    os.chdir(path)
    os.system("python3 " + path + "/" + ".nice.py")
tmux_create(BoxName, path)
---
date:   2024-07-16
tags:   linux, wsl, setup
---

# u24 on T14

## Basic install in custom location
Created the distro using the [wsl howto](../windows/wsl.md)

The files are in: `d:/_system/wsl/u24`
User: me/me (already sudo)
Hostname: u24
 
## Update and Generic Customization

Save installed apps list and update the system
```
sudo apt list --installed >  /mnt/d/_system/wsl/u24/
apt list --upgradable
```

Setup and test ssh/git
```
ln -s /mnt/c/Users/KatherineBarabash/.gitBashHome/.ssh ~/.ssh
chmod 600 ~/.ssh/*prv
chmod 644 ~/.ssh/config
ssh -T igh
ssh -T gh-me
ssh -T gh-i
```
`*TODO* repos on windows drive show dirty

Manually setup aliases, history and prompt by copying from the host 
*TODO* - 

## Python

First, checked what's there
```
which python
which python3       /usr/bin
python3 --version   3.12   
which pip
which pip3
sudo apt install python3-pip
```

To test, tried checking out and running `git@gh-me:Barabash-ka/pyutils.git`
Packages missing, tried to remember how to correctly create venv, tried looking for stored grep and find commands, then tried to install bashhub to look there. bashhub needed python 3.11 so left it to later (after wasting quite some time on it in gitbash) and proceeded without looking in own howtos.
Suceeded running `python -m cli.photos_organizer1` in both windows and linux !!!

### Other Python versions
bashhub wanted python less than 12:

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.11
which python3.11
curl -OL https://bashhub.com/setup && $SHELL setup --> fail
sudo apt-get install python3.11-distutils
curl -OL https://bashhub.com/setup && $SHELL setup --> ok
    registered as kathybarabash/commands4me
```

# did not do
sudo apt install build-essential -y
sudo apt install net-tools -y
# to get tree-like directory view
sudo apt install tree
#python 
# register alternatives
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2
# make choice
sudo update-alternatives --config python3
# dev
sudo apt install python3.12-dev 
# venv
sudo apt install python3.12-venv

```

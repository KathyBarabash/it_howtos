# Git


git remote add upstream git@igh:MCNM/observability.git
git remote -v
git branch --list
  
git fetch upstream
git pull upstream develop
git merge upstream/develop

git checkout -b new-br
git status
git log  
git add
git commit -s -m ""
git push origin new-br
PR in UI

git branch -d new-br
git push origin :new-br


git config --list --show-origin


---
https://www.guide2wsl.com/
on windows:
wsl --install -d Ubuntu-20.04
wsl -s Ubuntu-20.04
wsl 

c:/Users/KATHERINEBARABASH/.wslconfig
[wsl2]
memory=4GB  # Any size you feel like
swap=2GB
Processors = 4
localhostForwarding=true

/etc/wsl.conf
[network]
hostname = u20
generateHosts = false

[user]
default = me

https://sungkim11.medium.com/why-you-should-use-multiple-instances-of-same-linux-distro-on-wsl-windows-10-f6f140f8ed88
wsl --export Ubuntu-20.04 wsl-tars/u20base.tar.gz
wsl --import u20dev wsl-vms/u20dev wsl-tars/u20base.tar.gz


space issues with vhdx files https://nickjanetakis.com/blog/reclaiming-tons-of-diskspace-by-compacting-your-docker-desktop-wsl-2-vm

windows terminal configuration
settings.json is in C:\Users\KATHERINEBARABASH\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState

https://sungkim11.medium.com/why-you-should-use-multiple-instances-of-same-linux-distro-on-wsl-windows-10-f6f140f8ed88

---

sudo vi /etc/hosts

add to .bashrc to keep history 
TODO - expand to contain more info and copy to outside the host at logout for further reference
cat /mnt/c/0-GitBashHome/.bashrc_add >> .bashrc

# my customization 2022-01-11
# source - https://www.rootusers.com/17-bash-history-command-examples-in-linux/
# source - https://www.cyberciti.biz/faq/unix-linux-bash-history-display-date-time/
# source - https://spin.atomicobject.com/2016/05/28/log-bash-history/ - great source but otherwise nothing interesting
HISTIGNORE="top"
#HISTTIMEFORMAT="%c "
#HISTTIMEFORMAT="%d/%m/%y %T "
HISTTIMEFORMAT="%Y-%m-%d %H:%M "
[[ -d ~/.logs ]] || mkdir ~/.logs
#PROMPT_COMMAND='echo "$(date "+%Y-%m-%d.%H:%M:%S") $(pwd) $(history 1)" >> ~/.logs/bash-history-$(date "+%Y-%m-%d").log'
#PROMPT_COMMAND='echo "$(history 1)\t$(pwd)" >> ~/.logs/bash-history-$(date "+%Y-%m-%d").log'
PROMPT_COMMAND='echo "$(history 1) $(pwd)" >> ~/.logs/bash-history-$(date "+%Y-%m-%d").log'
PROMPT_COMMAND='echo "$(history 1)" >> ~/.logs/bash-history-$(date "+%Y-%m-%d").log'

other good settings that were there by default
# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

remove secure path so that sudo and normal paths do not differ
sudo vi /etc/sudoers
	comment out the secure_path setting
	add me ALL=(ALL) ALL
	
----
install the basics basics
sudo apt update && sudo apt -y upgrade
sudo apt install neofetch -y
sudo apt install build-essential -y
sudo apt install net-tools -y
sudo apt install golang-go -y
wget https://dl.google.com/go/go1.17.5.linux-amd64.tar.gz
sudo tar -xvf go1.17.5.linux-amd64.tar.gz -C /usr/local/
echo "PATH=/usr/local/go/bin:$PATH" >> ~/.bashrc

https://medium.com/geekculture/run-docker-in-windows-10-11-wsl-without-docker-desktop-a2a7eb90556d
sudo apt install docker.io -y

echo '# Start Docker daemon automatically when logging in if not running.' >> ~/.bashrc
echo 'RUNNING=`ps aux | grep dockerd | grep -v grep`' >> ~/.bashrc
echo 'if [ -z "$RUNNING" ]; then' >> ~/.bashrc
echo '    sudo dockerd > /dev/null 2>&1 &' >> ~/.bashrc
echo '    disown' >> ~/.bashrc
echo 'fi' >> ~/.bashrc

sudo usermod -aG docker $USER

docker run hello-world

https://medium.com/swlh/data-science-for-business-users-f4c050cbec96
---
if ui is needed
sudo apt install -y tasksel
sudo tasksel install xubuntu-desktop
sudo apt install gtk2-engines

export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0
export LIBGL_ALWAYS_INDIRECT=1
sudo /etc/init.d/dbus start &> /dev/null

in addition, need to install and start xserver on a host and configure the firewall
xserver and firewall like is explained here
https://techcommunity.microsoft.com/t5/windows-dev-appconsult/running-wsl-gui-apps-on-windows-10/ba-p/1493242
https://medium.com/@japheth.yates/the-complete-wsl2-gui-setup-2582828f4577

to check it works, see if firefox can be running-wsl-gui-apps-on-windows-10/ba-p/1493242

To install pycharm on linux:
sudo tar xzf /mnt/c/Users/KATHERINEBARABASH/Downloads/pycharm-community-2021.3.1.tar.gz -C /opt/
sh /opt/pycharm-community-2021.3.1/bin/pycharm.sh

---
softlink to .ssh and check permissions and connections
ln -s /mnt/c/0-GitBashHome/.ssh ~/.ssh
ls -latr ~/.ssh/
ssh -T igh to check connection to github.ibm

---
git
https://www.aleksandrhovhannisyan.com/blog/crlf-vs-lf-normalizing-line-endings-in-git/

https://www.aleksandrhovhannisyan.com/blog/atomic-git-commits/
https://www.aleksandrhovhannisyan.com/blog/undoing-changes-in-git/

git config --global core.autocrlf input
git config --global user.name "Katherine Barabash"
git config --global user.email kathy@il.ibm.com
git config --global help.autocorrect 1

https://opensource.com/article/20/10/advanced-git-tips
git rev-list –count master
git gc --prune=now --aggressive
git show main:README.md
git config --global -l

https://opensource.com/article/20/11/git-aliases
git config --global alias.p 'push'
git config --global alias.st 'status -sb'
git config --global alias.ll 'log --oneline'
git config --global alias.last 'log -1 HEAD --stat'
git config --global alias.cm 'commit -m'
git config --global alias.rv 'remote -v'
git config --global alias.gl 'config --global -l'

https://kbroman.org/github_tutorial/


https://kind.sigs.k8s.io/docs/user/using-wsl2/
git remote add origin git@github.com:<YOUR_REPOSITORY_ADDRESS>
git add .
git commit -m "first commit" 
git branch -M main
git push -u origin main

http://www.henryxi.com/git-merge-rebase
http://www.henryxi.com/git-delete-branch
http://www.henryxi.com/git-sync-remote-tag-to-local

● git status show the staging status and branch
● git branch <name> create a branch <name> pointing to the current commit. You are left
in the same branch or commit (detached state) you were.
● git branch --contains <commit> List all branches containing <commit>
● git checkout <name> switch to branch <name>.
● git checkout -b <name> will create a branch and check it out
	
	● git reset --hard [<commit>] unstages all files and restore
all (tracked) files to the state on commit (or HEAD)
● git checkout -f Roughly the same
	
● git log show the commit history of the current branch / detached mode
● git log <branch_name|tag|commit hash> show the commit history of a particular
● git log --oneline --graph Show the history of commits (only title) in a graph
● git log -p <branch_name|tag|commit hash> show commit history, including the diff of
each commit


http://www.henryxi.com/linux-often-used-commands-tutorial

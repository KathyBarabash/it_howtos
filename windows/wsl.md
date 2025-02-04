# WSL
(updated 2024-07-15 while working on fresh T14 windows11 installation)

## Just get going
`wsl` command comes preinstalled but not fully functional: 
- No useful `wsl` command (except for `wsl -l -o` or `wsl --help` can be run, not even `wsl -v` or `wsl --status` 
- Running just `wsl` will immediately install default distro in a default location
So the way to go is first install something and then move it to a convenient place to live 

```
wsl -l -o                     # to get list of available distros
wsl --install --d <distro>    # to install some distro; don't go away, will need to enter user/passsword

# in distro, can look around then exit
# now wsl output gets more meaningful
wsl -v       # version
wsl --status # status and version (warns about WSL1, need to enable this feature to get rid of the warning)
wsl --help   # more options than before
wsl -l -v    # list all the distros and their status      

# windows terminal now has profile for the installed distro
```

## Have distros in a specified place
First, stop the instance, export it to a desired location, and (optionally) unregister:
```
mkdir <wsl_distros_dir>
wsl -t <distro>
wsl --export <distro> <wsl_distros_dir>/<distro_name.tar>
wsl --unregister <distro>
```
Now can import the exported distro in the desired location with the desired name
```
wsl --import <name> <img_location> <wsl_distros_dir>/<distro_name.tar>
wsl -d <name> # to run
```

## Customize

### Global `.wslconfig` 
In %UserProfile% directory on Windows host
```
[wsl2]
memory=4GB 
swap=2GB
Processors = 4
localhostForwarding=true
```

### Per-instance `/etc/wsl.conf`
On windows, this file can be located in `\\wsl.localhost\<distro>\etc\wsl.conf`
```
## Automatically mount Windows drive when the distribution is launched
[automount]
# Set to true will automount fixed drives (C:/ or D:/) with DrvFs under the root directory set above. Set to false means drives won't be mounted automatically, but need to be mounted manually or with fstab.
enabled = true
# Sets the directory where fixed drives will be automatically mounted. 
root = <fill in the mnt point if different from /mnt/>
# DrvFs-specific options can be specified.  
options = "metadata,uid=1003,gid=1003,umask=077,fmask=11,case=off"
# Sets the `/etc/fstab` file to be processed when a WSL distribution is launched.
mountFsTab = true

## Network host settings that enable the DNS server used by WSL 2. This example changes the hostname, sets generateHosts to false, preventing WSL from the default behavior of auto-generating /etc/hosts, and sets generateResolvConf to false, preventing WSL from auto-generating /etc/resolv.conf, so that you can create your own (ie. nameserver 1.1.1.1).
[network]
hostname = <fill in the host name>
generateHosts = false
generateResolvConf = false

## Set whether WSL supports interop processes like launching Windows apps and adding path variables. Setting these to false will block the launch of Windows processes and block adding $PATH environment variables.
[interop]
enabled = false
appendWindowsPath = false

## Set the user when launching a distribution with WSL.
[user]
default = <fill in the user name>

## Set a command to run when a new WSL instance launches. This example starts the Docker container service.
[boot]
command = service docker start
systemd=true    # set by default in ubuntu24
```

### Convenience tips
Here is the updated 2024-07-16 experience with ubuntu 24, older info follows below.

- run system update
```
sudo apt update && sudo apt -y upgrade  # refresh the system
sudo apt autoremove
```

- system came with `/etc/wsl.config` file setting `systemd` to `true`. Edited it to also set host, network, mounting:
```
# was here by default this time
[boot]
systemd=true
###############################
[network]
hostname = u20
generateHosts = false
#generateResolvConf = false     <-- changed later

[user]
default = me

[automount]
options = "metadata"
```
Had to reboot with sudo `systemctl reboot`. 
All changes took effect, custom user added to sudo group.

- linked to .ssh on the host and had to change permisions 
```    
ln -s <path to .ssh> ~/.ssh            # create a link to ssh keys and configuration
ssh -T <igh>                           # failed due to permissions 

chmod 644 ~/.ssh/config
chmod 600 ~/.ssh/*.prv
ssh -T <igh>                           # failed due generateResolvConf = true

sudo systemctl reboot                  # modify config and reboot, soft link preserved!!!

me@u20:~$ ssh -T igh
Hi KATHY! You've successfully authenticated, but GitHub does not provide shell access.
me@u20:~$ ssh -T gh-me
Hi Barabash-ka! You've successfully authenticated, but GitHub does not provide shell access.
me@u20:~$ ssh -T gh-i
Hi KathyBarabash! You've successfully authenticated, but GitHub does not provide shell access.
```

- apply bash changes as in windows by just copying; TODO - create a sript so not to loose the existing ubuntu config
```
   56  2024-07-16 10:50:39 - alias gs='git status '
   57  2024-07-16 10:50:39 - alias ga='git add '
   58  2024-07-16 10:50:39 - alias gb='git branch '
   59  2024-07-16 10:50:39 - alias gcm='git commit'
   60  2024-07-16 10:50:39 - alias gd='git diff'
   61  2024-07-16 10:50:39 - alias gco='git checkout '
   62  2024-07-16 10:50:39 - #alias gl="git log log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
   63  2024-07-16 10:50:39 - #alias gl="git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
   64  2024-07-16 10:50:39 - alias more="less -de"
   65  2024-07-16 10:50:39 - # alias less='less -r'
   66  2024-07-16 10:50:39 - #alias ls='ls -F --color --show-control-chars'
   67  2024-07-16 10:50:39 - alias ll='ls -latr'
   68  2024-07-16 10:50:39 - alias h='history'
   69  2024-07-16 10:50:39 - alias gh='history | grep'
   70  2024-07-16 10:50:42 - ll
   71  2024-07-16 10:51:34 - gh ln
   72  2024-07-16 10:52:16 - ln -s /mnt/c/Users/KatherineBarabash/.gitBashHome/.bash_hist/ ~/.bash_hist
   73  2024-07-16 10:52:46 - HISTDIR_NAME="$HOME/.bash_hist"
   74  2024-07-16 10:52:46 - mkdir -p $HISTDIR_NAME
   75  2024-07-16 10:52:46 - HISTFILE_NAME="$HISTDIR_NAME/hist_$HOSTNAME"
   76  2024-07-16 10:52:46 - test -f $HISTFILE_NAME || touch $HISTFILE_NAME
   77  2024-07-16 10:52:54 - echo HISTDIR_NAME
   78  2024-07-16 10:53:02 - echo $HISTDIR_NAME
   79  2024-07-16 10:53:11 - ll $HISTDIR_NAME
   80  2024-07-16 10:53:30 - echo $HISTFILE_NAME
   81  2024-07-16 10:54:01 - export HISTSIZE=-1
   82  2024-07-16 10:54:01 - export HISTFILESIZE=-1
   83  2024-07-16 10:54:01 - export HISTTIMEFORMAT='%F %T - '
   84  2024-07-16 10:54:01 - export HISTCONTROL=ignoreboth
   85  2024-07-16 10:54:01 - export HISTIGNORE="clear:history:[bf]g:exit:date:* --help"
   86  2024-07-16 10:54:01 - export PROMPT_COMMAND='history -a'
   87  2024-07-16 10:54:01 - shopt -s histappend
   88  2024-07-16 10:54:01 - export HISTFILE=$HISTFILE_NAMEexport HISTSIZE=-1
   89  2024-07-16 10:54:01 - export HISTFILESIZE=-1
   90  2024-07-16 10:54:01 - export HISTTIMEFORMAT='%F %T - '
   91  2024-07-16 10:54:01 - export HISTCONTROL=ignoreboth
   92  2024-07-16 10:54:01 - export HISTIGNORE="clear:history:[bf]g:exit:date:* --help"
   93  2024-07-16 10:54:01 - export PROMPT_COMMAND='history -a'
   94  2024-07-16 10:54:01 - shopt -s histappend
   95  2024-07-16 10:54:01 - export HISTFILE=$HISTFILE_NAME
   96  2024-07-16 10:54:08 - ls
   97  2024-07-16 10:54:16 - more $HISTFILE_NAME
   98  2024-07-16 10:54:23 - gh ll
   99  2024-07-16 10:54:38 - function parse_git_dirty {   [[ $(git status --porcelain 2> /dev/null) ]] && echo "*"; }
  100  2024-07-16 10:54:38 - function parse_git_branch {   git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e "s/* \(.*\)/ (\1$(parse_git_dirty))/"; }
  101  2024-07-16 10:54:38 - export PS1="\n\t \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
```

- TODO set variable to point to wsl home to save important artifacts 

- TODO git repos cloned on win show changes on u24

- TODO setup python

- TODO check old scripts

[text](../../extracted/wslhome-plus/wsl-new-distro.sh) [text](../../extracted/0-GitBashHome/u20-dev/install-docker.sh) [text](../../extracted/0-GitBashHome/u20-dev/install-go.sh) [text](../../extracted/0-GitBashHome/u20-dev/install-kubectl.sh) [text](../../extracted/0-GitBashHome/u20-dev/setup-dev.sh) [text](../../extracted/0-GitBashHome/u20-dev/startDocker.sh) [text](../../extracted/0-GitBashHome/u20-dev/start-docker.sh) [text](../../extracted/0-Home-save/test.sh) [text](../../extracted/0-Home-save/test1.sh) [text](../../extracted/0-Home-save/test2.sh) [text](../../extracted/0-Home-save/zero2hero.sh) [text](../../extracted/ibmgh/connector/notebooks/generated-code/git_push.sh) [text](../../extracted/pyml/scripts/toc.sh) [text](../../extracted/pyml_repos/pubgh/data-demo/install.sh) [text](../../extracted/wslhome-plus/mbg-setup.sh) [text](../../extracted/wslhome-plus/wsl-mod-instance.sh)


## Old Experience

at some `wsl-new-distro.sh` script was created to perform the actions listed below.
Maybe outdated now, needs review before executing on new host machine.
```
me@IBM-PF346ZVH:~$ cd /mnt/d/.home/
me@IBM-PF346ZVH:/mnt/d/.home$ . wsl-new-distro.sh u20base
```

### Allow the new user to run sudo commands without password
```
sudo visudo /etc/sudoers
```

Add this line: `<user>  ALL=(ALL) NOPASSWD:ALL` and save the modified file.
  
- Set `root` account 
```
sudo passwd root
```
  
#### Configure WLS on Linux 
Create or edit `/etc/wsl.conf` file to configure basic behavior.
Should work smoothly but if there are problems, try:

- If wsl.conf calls for setting custom hostname, change it also in the system by editing `/etc/hosts` file
```
# to enforce changing host name
sudo vi /etc/hostname       

# to fix permissions for mounted windows files 
sudo umount /mnt/c
sudo mount -t drvfs C: /mnt/c -o metadata
```
    
#### Customize and install the most basic tools, e.g. by running the commands below or the `setup-base.sh` script:
```
sudo apt update && sudo apt -y upgrade  # refresh the system
sudo apt autoremove
sudo apt install neofetch -y
    
sudo apt install build-essential -y     # basic installs
sudo apt install net-tools -y
    
ln -s <path to .ssh> ~/.ssh            # create a link to ssh keys and configuration
ssh -T <igh>                            # verify ssh settings trying to connect to git
```

#### To run GUI applications
Might be very outdated, check before using
Sources:
- https://techcommunity.microsoft.com/t5/windows-dev-appconsult/running-wsl-gui-apps-on-windows-10/ba-p/1493242
- https://medium.com/@japheth.yates/the-complete-wsl2-gui-setup-2582828f4577

```
sudo apt install xrdp -y && sudo systemctl enable xrdp

sudo apt install -y tasksel
sudo tasksel install xubuntu-desktop
sudo apt install gtk2-engines

export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0
export LIBGL_ALWAYS_INDIRECT=1
sudo /etc/init.d/dbus start &> /dev/null

now could run firefox in a separate window

sudo tar xzf /mnt/c/Users/KATHERINEBARABASH/Downloads/pycharm-community-2021.3.1.tar.gz -C /opt/
sh /opt/pycharm-community-2021.3.1/bin/pycharm.sh
```

## Related
  
### Windows Terminal configuration
Resides in `settings.json` file in `C:\Users\KATHERINEBARABASH\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState`
Can be modified by editing the above file directly or through TW settings interface.

## References
- [Oficial documentation](https://docs.microsoft.com/en-us/windows/wsl/)


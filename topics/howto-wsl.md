# WSL setup

## Links

- [Oficial documentation](https://docs.microsoft.com/en-us/windows/wsl/)

## Prerequisites

Good to install and configure before WSL:
- Windows terminal
  - [Relative link to WT setup howto](howto-winterm.md) 
  - [Absolute link to WT setup howto](https://github.com/KathyBarabash/howto/blob/main/topics/howto-winterm.md)
- VScode 

## Install the __WSL__ 

WSL is installed with `wls` command line utility, run in a terminal with evelated priviledges ( __run as administrator__).
  ```
  wsl                       # to see the command line options 
                            # only before WSL installation
                            # later, this command will launch the default distro)
                            
  wsl -l -o                 # to see distros available for installation; default distro is marked with `*`
  
  wsl --install             # to install WSL with the default distro
                            # only before WSL installation
                            # later, -d parameter is required
                            
  wsl --install -d <distro> # to install (WSL with) the distro of choice
  ```  
  
When run for the first time, the `wsl --install` command installs WSL internals and brings the distro of choice. System restart is required. After the restart, the distro is installed and can be communicated to in a dedicated window. In addition, new WT profile for a new distro is automatically created. 

## Configure the __WSL__

WSL is controlled by the 'global' WSL configuration settings by editing the `.wslconfig` file in `user home` directory on Windows host and by the 'per-instance' WSL configuration setting in `/etc/wsl.conf` of each specific Linix instance.

- Global `.wslconfig` on Windows host
```
[wsl2]
memory=4GB 
swap=2GB
Processors = 4
localhostForwarding=true
```

- Per-instance `/etc/wsl.conf`
```
[network]
hostname = <fill in the host name>
generateHosts = false

[user]
default = <fill in the user name>

[automount]
root = <fill in the mnt point if different from /mnt/>
options = "metadata"
  ```

## Install and manage Linux distros

To manage WSL and its distros, the same `wsl` command line utility is used:
```
wsl -l -o                     # list distros available for installation
wsl -l                        # list the installed instances 
wsl -l -v                     # list the installed instances and their status

wsl --install -d <distro>     # install instance of the distro of choice

wsl                           # start default instance
wsl -d <instance>             # start the specified instance
wsl -s <instance>             # set the default instance

wsl -t <instance>             # stop the specified instance
wsl --shutdown                # stop all the instances and WSL processes
wsl --unregister <instance>   # remove the specified instance from the system and free up its resources

```

## Work with WSL Distros

When new Linux instance is installed it can be communicated to for the initial setup in a dedicated terminal window. 
The system will request you to set user/password and will create a new Windows Terminal profile. 
By default, windows file system is mounted to the new instance at `/mnt`.

### Customize Instances
  
- Allow the new user to run sudo commands without password
```
sudo visudo /etc/sudoers
```

Add this line: `<user>  ALL=(ALL) NOPASSWD:ALL` and save the modified file.
  
- Set `root` account 
```
sudo passwd root
```
  
- Configure WLS on Linux - create `/etc/wsl.conf` file and , optionally, assign custom hostname:
```
[network]
hostname = u20dev           # CHANGE to your value
generateHosts = false       # this will prevent wsl from editing /etc/hostname and /etc/hosts files 

[user]
default = me                # CHANGE to your value

[automount]
root = /win                 # where to mount windows FS
options = "metadata"        # allow modifying windows FS metadata, e.g. permissions
```
    
- If wsl.conf calls for setting custom hostname, change it also in the system by editing `/etc/hosts` file
```
sudo vi /etc/hostname
```
- If there are problems with file permissions, try:
```
sudo umount /mnt/c
sudo mount -t drvfs C: /mnt/c -o metadata
```
    
- Customize and install the most basic tools, e.g. by running the commands below or the `setup-base.sh` script:
```
sudo apt update && sudo apt -y upgrade  # refresh the system
sudo apt autoremove
sudo apt install neofetch -y
    
sudo apt install build-essential -y     # basic installs
sudo apt install net-tools -y
    
ln -ls <path to .ssh> ~/.ssh            # create a link to ssh keys and configuration
ssh -T <igh>                            # verify ssh settings trying to connect to git
    
```

### Manage Multiple Instances
Now you can either continue working with the new distro or exit and do few more steps to allow installing multiple instances of the same distro.

1. Preapare local reusable image of this distro

    1. Stop the running distros
    ```
    wsl --shutdown
    ```

    1. Export the primed distro to the know location for creating additional instances:
    ```

    ```

    1. Optionally, unregister the original instance from the system 
    ```
    wsl --unregister -d <distro>
    ```

1. Create new instance from the saved tarballs
  ```

  ```
  Remember to update the hostname of the new instances by editing `/etc/hosts` and `/etc/wsl.conf` files.

## Related
  
### Windows Terminal configuration
Resides in `settings.json` file in `C:\Users\KATHERINEBARABASH\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState`
Can be modified by editing the above file directly or through TW settings interface.

### To run GUI applications
xserver and firewall
https://techcommunity.microsoft.com/t5/windows-dev-appconsult/running-wsl-gui-apps-on-windows-10/ba-p/1493242

on newly installed distro
https://medium.com/@japheth.yates/the-complete-wsl2-gui-setup-2582828f4577

sudo apt update && sudo apt -y upgrade

sudo apt install neofetch
sudo apt install build-essential
sudo apt install net-tools
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

---

  


# WSL setup

Good to install and configure before WSL:
- Windows terminal; [howto](howto-winterm.md) [link](https://github.com/KathyBarabash/howto/blob/main/topics/howto-winterm.md)
- VScode 

## Install the __WSL__ 

Installing WSL became easier with new Windows releases and the only thing to do is to run the following command __as administrator__
  ```
  wsl --install
  ```
This command installs the default distro that can be removed later if not wanted.

> __TODO__ check whether `wsl -l -o` can be run before `wsl --install` for choosing the desired distro

## Configure the __WSL__

Define global WSL configuration settings by editing the `.wslconfig` file in user home directory:
  ```
  [wsl2]
  memory=4GB 
  swap=2GB
  Processors = 4
  localhostForwarding=true
  ```

## Install and manage Linux distros

1. Find out what distros are available
    ```
    wsl -l -o
    ```
1. Install the distro of choice; the installation will start in a separate window and will request to set up the user account.
    ```
    wsl --install -d <distro>
    ```
    
1. After creating the user account, do initial customization with these few additional usefull steps:

  1. Edit `/etc/sudoers` file to allow the new user to run sudo commands without password.
  1. Set `root` account with 
    ```
    sudo passwd root
    ```
  
  1. Create `/etc/wsl.conf` file and , optionally, assign custom hostname:
    ```
    [network]
    hostname = u20dev           # CHANGE to your value
    generateHosts = false       # this will prevent wsl from editing /etc/hostname and /etc/hosts files so we can set our own hostname by editing /ect/hosts file once

    [user]
    default = me                # CHANGE to your value

    [automount]
    root = /win                 # where to mount windows FS
    options = "metadata"        # allow modifying windows FS metadata, e.g. permissions; 
    ```
    
    If wsl.conf calls for setting custom hostname, change it also in the system by editing `/etc/hosts` file
    ```
    sudo vi /etc/hostname
    ```
    If there are problems with file permissions, try:
    ```
    sudo umount /mnt/c
    sudo mount -t drvfs C: /mnt/c -o metadata
    ```
    
  1. Customize and install the most basic tools, e.g. by running the commands below or the `setup-base.sh` script:
    ```
    
    sudo apt update && sudo apt -y upgrade  # refresh the system
    sudo apt autoremove
    sudo apt install neofetch -y
    
    sudo apt install build-essential -y     # basic installs
    sudo apt install net-tools -y
    
    ln -ls <path to .ssh> ~/.ssh            # create a link to ssh keys and configuration
    ssh -T <igh>                            # verify ssh settings trying to connect to git
    
    ```
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

## Brief command reference
  ```
  wsl -l -v                     # list all the instances and their status
  wsl --shutdown                # stop all the instances
  wsl -s <instance>             # set the default instance
  wsl                           # stare default instance
  wsl -d <instance>             # start the specified instance
  wsl -t <instance>             # stop the specified instance
  wsl --unregister <instance>   # remove the specified instance from the system and free up its resources
    
  ```
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

  


2023-02-21 Installing Palmetto GW on WSL2, u20work as me

GITHUB_TOKEN=[removed, starts with ghp_] M41lv WpB2Su5X B1ZnD fClG3a 2D0D21 KcPMl
export ARTIFACTORY_APIKEY=[removed] AKCp8jQ TdL1VH ZinXTDrbrqyXU1f LSCAmpyuLh3q S5s7kLf h1cSXtbyGzT qXSdD BWfvb 29C1u

\\wsl$\Ubuntu-22.04.
Liran: find -name "*.*" |  xargs grep -i dirname

cd ../pgw/gateway/tools/setup/
. setup_go_env.sh
gvm use go1.19.5
. setup_docker.sh
. setup_linter.sh
. setup_shfmt.sh
. setup_yq.sh
. setup_dep.sh

. setup.sh

me@u20work:/mnt/d/.home$ cd ../pgw/gateway/
me@u20work:/mnt/d/pgw/gateway$ make setup
./tools/setup/check_versions.sh: line 18: /home/me/.gvm/pkgsets/go1.19.5/global/bin/gosec: No such file or directory
securego/gosec info checking GitHub for tag 'v2.14.0'
securego/gosec info found version: 2.14.0 for v2.14.0/linux/amd64
securego/gosec info installed /home/me/.gvm/pkgsets/go1.19.5/global/bin/gosec
Installed/updated git pre-commit hook
Installed/updated git commit-msg hook




- Clone https://github.ibm.com/palmetto/gateway to d:/pgw

- Follow dev setup instructions on https://github.ibm.com/palmetto/gateway/blob/develop/doc/dev-setup.md

- . setup_go_env.sh: Checks that Go is installed and if using GVM it sets the environment to use Go 1.19.1
	- needs gvm AND go to be installed on the system otherwise throws cryptic errors!!!
	```
	bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
	
	sudo apt install golang-go
	```
	- dirname issue not understanding the command line
	```
	source $(dirname -- "$0")/utils.sh
	```
	- maybe there are issues with login/user permissions and shell (maybe related to WSL only)
	```
	gvm use go1.19.5
	```

- setup_docker.sh

	```
	Synchronizing state of docker.service with SysV service script with /lib/systemd/systemd-sysv-install.
	Executing: /lib/systemd/systemd-sysv-install enable docker
	System has not been booted with systemd as init system (PID 1). Can't operate.
	Failed to connect to bus: Host is down
	[process exited with code 1 (0x00000001)]
	
	change sysctl commands to 
	sudo /etc/init.d/docker start
	```
	
	- enable systemd https://devblogs.microsoft.com/commandline/systemd-support-is-now-available-in-wsl/
	
- go
```
sudo apt-get install curl git mercurial make binutils bison gcc build-essential python3.6 python-jinja2
	bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
	source /home/jlearman/.gvm/scripts/gvm
	gvm install go1.4 -B
	gvm use go1.4
	gvm install go1.19.1
	gvm use go1.19.1
```

- make 
	kernel?

- tokens

- git

- frr image

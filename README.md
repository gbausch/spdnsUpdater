# spdnsUpdate -- Securepoint DNS Updater
Python script based on [Michael Nowak's script](https://gist.github.com/mmichaa/5587307) to update IP addresses on [Securepoint Dynamic DNS Service](https://spdyn.de).

**Usage:**
- ```python spdnsUpdate.py <hostname> <user> <password>```
- ```python spdnsUpdate.py <hostname> <token>```

In case you want to auto update the device ip address at every reboot, insert one of the lines above in ```/etc/rc.local``` (Linux only).

**Required Python packages:** ```get``` and ```requests```. Install with:
* ```pip install get```
* ```pip install requests```

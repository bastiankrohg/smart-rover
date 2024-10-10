# Rover
Robotics project - final year INSA Toulouse

details of assembly : https://4tronix.co.uk/blog/?p=2112
Rover coding examples : https://github.com/4tronix/MARS-Rover
How to set up static ip on raspberry pi: https://www.youtube.com/watch?v=d1y1ZIIX-XQ&t=293s

Pi zeros are currently configured to work with Bastian's home wifi. This can be changed by 1) Rewriting the SD card with new network name & password using raspberry imager or 2) using "sudo raspi-config" after establishing a remote connection

### IP Addresses
IP @ rover : 192.168.0.168 [TODO]
IP @ rover2 : 192.168.0.169

### Connecting remotely to rovers
Rover: ssh rover@rover.local **or** ssh rover@192.168.0.168

Rover2: ssh rover2@rover2.local **or** ssh rover2@192.168.0.169

how to connect to the raspberry :
![image](https://github.com/user-attachments/assets/ab559dd2-974e-4bb3-a19c-3d8b0c0d7cd0)


### Adding git ssh verification for raspberry pi
First, ensure that the git repo is cloned using ssh, not https to avoid having to reconfigure the "remote.origin.url".
If need be, use the following command: git config remote.origin.url "git@github.com:bastiankrohg/smart-rover.git"
Generate key and add to git:
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=linux

Ensure user.email + user.name is set globally, if requested.



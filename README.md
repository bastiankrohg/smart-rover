# Rover
Robotics project - final year INSA Toulouse

## Things we might want to check out
https://medium.com/home-wireless/headless-streaming-video-with-the-raspberry-pi-zero-w-and-raspberry-pi-camera-38bef1968e1
https://www.linux-projects.org
https://www.linux-projects.org/uv4l/object-detection-with-depth-estimation/
https://github.com/Qengineering/TensorFlow_Lite_Classification_RPi_zero

# Nice to have
## Adding several known wifis
https://raspberrypi.stackexchange.com/questions/11631/how-to-setup-multiple-wifi-networks

## Export files from raspberry pi
scp rover@\<IP Address of Raspberry Pi>:\<Path to File> 

## Safely shut down raspberry pi
sudo halt -p
or: sudo poweroff
or: sudo shutdown -h now 

## Controlling the raspberry pi camera
Guide: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/3

## Set up rtsp stream for raspi and raspicam
https://github.com/bluenviron/mediamtx?tab=readme-ov-file#rtsp-cameras-and-servers
Install mediamtx, set up using [this guide]([url](https://james-batchelor.com/index.php/2023/11/10/install-mediamtx-on-raspbian-bookworm/))
NB! I lowered the bitrate and the resolution because with the configuration in James' example it crashed (not sure if internet repeater or pi zero who crashed).
I now use 
paths:
  cam:
    source: rpiCamera
    rpiCameraWidth: 640 # instead of 1080
    rpiCameraHeight: 480 # instead of 720
    rpiCameraVFlip: true
    rpiCameraHFlip: true
    rpiCameraBitrate: 500000 # instead of 1500000

# Assembly and setup information
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

### Rover python guide
- https://4tronix.co.uk/blog/?p=2409

### Known Issues
#### Testing Rover with python examples from 4tronix:
SETUP & TEST ROVER - Missing packages to run calibrateServos.py:
First create a venv and activate it -> link: https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://docs.python.org/3/library/venv.html&ved=2ahUKEwiMwJet44aJAxVkfKQEHfyqNXAQFnoECAgQAQ&usg=AOvVaw1SQ6VGTcJCX7W6wOs1SpnV
- missing rpi-ws281x -> sudo pip install rpi-ws281x --break-system-packages
- missing RPi.GPIO -> pip install RPi.GPIO
- pip3 install smbus
- smbus.SMBus(1) FileNotFoundError: No such file or directory -> Activate i2c interface using sudo raspi-config -> interface -> enable (enable both i2c & SPI)
- ...



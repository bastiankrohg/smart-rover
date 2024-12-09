# Rover Project

Robotics project for the final year at INSA Toulouse, featuring a modular system for hardware control, mapping, and vision-based autonomous/semi-autonomous navigation.

## 1. Overview

This repository serves as the main entry point for the project, which is structured into the following submodules:

- **[Rover-Pi](https://github.com/bastiankrohg/rover-pi):** Handles hardware control (motors, sensors, camera).
- **[Rover-Coral](https://github.com/bastiankrohg/rover-coral):** Manages higher-level logic and mapping functionality, leveraging the Google Coral Dev Board.
- **[Rover-Protos](https://github.com/bastiankrohg/rover-protos):** Contains the gRPC proto definitions for communication between modules.
- **[Rover-Vision](https://github.com/bastiankrohg/rover-vision):** Handles computer vision testing and model training.

Each submodule contains its own README with detailed setup and usage instructions.

## 2. Features

- Modular design with gRPC-based communication.
- Real-time mapping and path tracing.
- Remote control with hardware interfacing for sensors and motors.
- RTSP video streaming from the PiCamera2 on the Raspberry Pi Zero.
- Testing and training of computer vision models for resource detection.

## 3. Quick Start Guide

### Cloning the Repository with Submodules
```bash
git clone --recurse-submodules git@github.com:bastiankrohg/smart-rover.git
cd smart-rover
```
If submodules are not cloned, initialize them:
```bash
git submodule update --init --recursive
```

### Setting Up the Environment

1. Follow the setup instructions in the respective submodules:
   - [Rover-Pi Setup](https://github.com/bastiankrohg/rover-pi#readme): Configure and control the rover's hardware.
   - [Rover-Coral Setup](https://github.com/bastiankrohg/rover-coral#readme): Manage mapping, gRPC communication, and high-level control.
   - [Rover-Vision Setup](https://github.com/bastiankrohg/rover-vision#readme): Train and test computer vision models for resource detection.
   - [Rover-Protos Setup](https://github.com/bastiankrohg/rover-protos#readme): Update and compile gRPC protobufs.

2. Configure communication:
   - Assign static IPs for the Raspberry Pi and Coral Dev Board.
   - Ensure the devices can communicate over the same local network.

### Running the System

1. **Start Hardware Control:**
   - Launch the `rover-pi` control script on the Raspberry Pi:
     ```bash
     python3 rover-pi/pi_v2.py
     ```

2. **Start Mapping and Control:**
   - Launch the `rover-coral` mapping and control module on the Coral Dev Board:
     ```bash
     python3 rover-coral/control.py
     ```

3. **Access RTSP Stream:**
   - View the live video stream from the PiCamera2 at:
     ```
     rtsp://<pi-ip>:5054/cam
     ```
   - Replace `<pi-ip>` with the actual IP address of the Raspberry Pi.

4. **Interact with the Rover:**
   - Use gRPC clients or manual scripts to control movement and mapping.

## 4. RTSP Streaming with Mediamtx

The Raspberry Pi Zero streams video from the PiCamera2 using [Mediamtx](https://github.com/bluenviron/mediamtx).

- **Configuration:**
  - Resolution: 640x480
  - Bitrate: 500 kbps
  - Horizontal and vertical flip enabled for correct orientation.

- **Access:**
  - Stream Address: `rtsp://<pi-ip>:5054/cam`

Mediamtx is installed as a systemd service and starts automatically on boot.

## 5. Future Improvements

- **Integration:**
  - Synchronize mapping and hardware control for seamless operation.

- **Autonomous Navigation:**
  - Implement algorithms for obstacle detection, path planning, and search patterns.

- **Telemetry Dashboard:**
  - Develop a dashboard to display real-time rover telemetry and performance metrics.

- **Enhanced Calibration:**
  - Integrate odometry data from motor encoders for precise movement tracking.

- **Vision-Based Navigation:**
  - Incorporate trained models from `rover-vision` for real-time decision-making.

## 6. Archived Notes

### References
- [4tronix Assembly Guide](https://4tronix.co.uk/blog/?p=2112)
- [Raspberry Pi OS](https://www.raspberrypi.com/software/operating-systems/)
- [Programming M.A.R.S. Rover](https://4tronix.co.uk/blog/?p=2409)

### SSH Configuration
- **Default IPs:**
  - `Rover`: 192.168.0.168
  - `Rover2`: 192.168.0.169
- Connect via:
  ```bash
  ssh rover@192.168.0.168
  ```
- Safe Shutdown
  ```bash
  sudo shutdown -h now
  ```
- Adding Known Wi-Fi Networks
  - [Setting up multiple known wifi networks]([https://4tronix.co.uk/blog/?p=2112](https://raspberrypi.stackexchange.com/questions/11631/how-to-setup-multiple-wifi-networks))

- Troubleshooting
  - Missing python packages:
  ```bash
  pip install rpi-ws281x RPi.GPIO smbus
  ```
  - Missing I2C/SPI configuration:
  Enable in sudo raspi-config.

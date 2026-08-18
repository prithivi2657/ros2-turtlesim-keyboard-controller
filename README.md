# ROS 2 TurtleSim Keyboard Controller

## Project Description

This project implements a custom ROS 2 Jazzy Python node to control the TurtleSim robot using keyboard commands.

## Controls

| Key | Action |
|-----|--------|
| A | Move forward |
| R | Rotate continuously |
| S | Stop |
| Q | Quit |

## Requirements

- Ubuntu
- ROS 2 Jazzy
- Python 3
- turtlesim

## Build

```bash
cd ~/turtle_ws
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash

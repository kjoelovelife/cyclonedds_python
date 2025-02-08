![Version](https://img.shields.io/badge/version-v0.0.1-success)
###### tags: `Brogent` `ROS2` `controller_plugin`

# kjoelovelife-CycloneDDS Python
This repository is dedicated to using CycloneDDS.  
An auto-install script will be added in the future.

# Resources
- [Eclipse Cyclone DDS offical site](https://cyclonedds.io/) 
- [Eclipse Cyclone DDS repo](https://github.com/eclipse-cyclonedds)


If you want to use Python API:
- [Setup Guide for Cyclone DDS Python API](https://dds-demonstrators.readthedocs.io/en/latest/Teams/1.Hurricane/setupDDSPython.html)
- [cyclonedds-python repo](https://github.com/eclipse-cyclonedds/cyclonedds-python)

# Hints
- Define common message types in a shared module rather than creating them in multiple files.
- Command Line Tools (CLI) support specifying a domain ID.
- To connect with ROS2-Humble, the topic name must be prefixed with `rt/`

# Next
- Build proper Message Type for both ROS2-Humble and CycloneDDS.


# Developer log
- Author: WeiChih Lin(weichih.lin@protonmail.com)

| Date | State |
|------|-------|
| 2025/02/03| First Commit.|
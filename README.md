# Raspberry Pi Traffics Lights

This is for all the moms and dads out their that want to teach and show their kids the joy of tech and programming. This repository contains all the info and files from my first project with my eldest daughter. For some reason, she wanted to build a traffic light. Well, here we go!

## Hardware

The basic hardware I ordered are the following two things. Additionally, you will need a
micro SD card and a suitable 5 V/DC 2500 mA power supply.

- [JAM HAT (LED & Buzzer Board)](https://www.modmypi.com/raspberry-pi/led-displays-and-drivers-1034/jam-hat)
- [Conrad Components Set Raspberry Pi](https://www.conrad.de/de/lernpaket-conrad-components-set-raspberry-pi-verstehen-und-anwenden-inkl-raspberry-pi-3-1517943.html)

## Quick Start (Day 1)

On the first day we focused on the assembly of all parts and the basic setup of the Pi and the Jam HAT hardware.

1. First, we downloaded the latest Raspbian release from https://www.raspberrypi.org/downloads/raspbian/. We went for the *Raspbian Stretch with desktop and recommended software* release.

2. Then, we flashed the downloaded image using [balenaEtcher](https://www.balena.io/etcher/). It can flash the downloaded ZIP archive directly, without unpacking.

3. We unpacked the hardware. My daughter then assembled the Raspberry Pi together with the Jam HAT board. I showed her how to connect the HDMI cable, insert the micro SD card and finally how to connect the power.

4. We then did the basic system setup. To get this done quickly, I did most of it. Setting up the proper language and Wifi seems rather boring to an 8 year old girl.

5. Finally, we were ready to test drive the Jam HAT hardware. We cloned the official demo repository (https://github.com/modmypi/Jam-HAT) and ran the different samples together.

After looking the the Python code, I realized that it might be a bit too early to teach my daughter a programming language. And Python 2 will definitely not be her first one! ;)


## Traffic Lights with Scratch 2

So I had a look at Scratch 2. Fortunately, there is the possibility to do basic GPIO programming visually, see https://www.raspberrypi.org/documentation/usage/gpio/scratch2/README.md

## Traffic Lights with Node-RED

## Advanced: Programming

Of course, I was also keen on programming the Jam HAT. The official demo files of the Jam HAT were written in Python 2. So at least I wanted to use something more modern.

### Using Jam HAT with Python 3

### Using Jam HAT with Node.js

## References

- http://wiringpi.com/pins/
- https://projects.raspberrypi.org/de-DE/jam/jam
- https://www.npmjs.com/package/temporal
- https://github.com/nebrius/raspi-io/
- http://johnny-five.io
- https://www.modmypi.com/raspberry-pi/led-displays-and-drivers-1034/jam-hat
- https://www.raspberrypi.org/documentation/usage/gpio/scratch2/README.md


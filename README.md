## Description
Lux Infinitum is simple tool to control an Arduino-powered LED strip (strips?) over USB via a Python script.

## Setup
### Arduino
* Set up an Arduino with a NeoPixel LED strip using the USB power diagram:
** (Arduino wiring diagram)[https://www.eerkmans.nl/powering-lots-of-leds-from-arduino/]
* Power up your LED strip and connect your Arduino to your machine via USB
* Open `lux-infinitum.ino` in the Arduino IDE.
* Install the "Adafruit NeoPixel" library in the Arduino IDE (v1.3.5 at time of writing).
* Compile and deploy `lux-infinitum.ino` to your Arduino device.

### Python
```
source env/bin/activate
pip install -r requirements.txt
```

## How to run
```
python lux-infinitum.py
```
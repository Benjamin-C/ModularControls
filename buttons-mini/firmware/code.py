# import neopixel_simpletest

from setup import *

# ------------------------------------------------------------------
#     BEGIN USER CONFIG SECTION
#
#   Configure how the buttons work.
#   keyMapping sets the direction that the cable goes
#   onPress and onRelease are arrays of functions that get called
#       when a key is pressed or released. They are given the
#       number of the LED that corresponds to that key.
#       pixels.brightness controls the brightness of the pixels
#   You can add any other functions you want in this section
# ------------------------------------------------------------------

# Set wether the cable goes UP, DOWN, LEFT, or RIGHT
# This makes the keys always go L>R T>B in the onPress and onRelease below
# IMPORTANT Do not delete this variable.
keyMapping = CABLE_UP_MAP

# Light brightness, use number from 0 to 1 637.605.36
pixels.brightness = 0.8

# Imports for keyboard actions
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
kbddev = Keyboard(usb_hid.devices)
kbd = KeyboardLayoutUS(kbddev)

toType = ["7", "8", "9", "\b", "4", "5", "6", "-", "1", "2", "3", "", "0", "0", ".", " & "]

# Turn on a light then update all the lights
def setLight(i, c):
    pixels[i] = c
    pixels.show()

# Do what happens when a key is pressed
def doPress(i, text):
    setLight(i, (255, 0, 255))
    kbd.write(text)

# Do what happens when a key is released
def doRelease(i):
    setLight(i, (128, 32, 0))
    # setLight(i, (255, 128, 0))

# onPress is an array of functions to call when the button is pressed.
# The button order is L>R T>B, based on the setting of keyMapping.
# i is the LED number
# IMPORTANT Do not delete this array.
onPress = [
    lambda i : doPress(i, toType[0x0]),
    lambda i : doPress(i, toType[0x1]),
    lambda i : doPress(i, toType[0x2]),
    lambda i : doPress(i, toType[0x3]),
    lambda i : doPress(i, toType[0x4]),
    lambda i : doPress(i, toType[0x5]),
    lambda i : doPress(i, toType[0x6]),
    lambda i : doPress(i, toType[0x7]),
    lambda i : doPress(i, toType[0x8]),
    lambda i : doPress(i, toType[0x9]),
    lambda i : doPress(i, toType[0xA]),
    lambda i : doPress(i, toType[0xB]),
    lambda i : doPress(i, toType[0xC]),
    lambda i : doPress(i, toType[0xD]),
    lambda i : doPress(i, toType[0xE]),
    lambda i : doPress(i, toType[0xF])
]

# onRelease is an array of functions to call when the button is released.
# The button order is L>R T>B, based on the setting of keyMapping.
# i is the LED number
# IMPORTANT Do not delete this array.
onRelease = [
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i),
    lambda i : doRelease(i)
]

# Turn on all the lights as if all the buttons have just been released
for i in range(len(onRelease)):
    doRelease(i)

# ------------------------------------------------------------------
#     END USER CONFIG SECTION
# ------------------------------------------------------------------
# Don't modify anything below here unless you know what you're doing

# Setup each button
for pinNum in buttonPins:
    pin = digitalio.DigitalInOut(pinNum)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    switch = Debouncer(pin)
    rawButtons.append(pin)
    buttons.append(switch)

# Run the buttons
while True:
    for i in range(len(buttons)):
        switch = buttons[i]
        switch.update()
        mapNum = keyMapping[i]
        # Switches are active low
        if switch.rose: # Switch released
            onRelease[mapNum](i)
        if switch.fell: # Switch pressed
            onPress[mapNum](i)
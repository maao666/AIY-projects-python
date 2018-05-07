#!/usr/bin/env python3
"""Monitor the button and perform shutdown 
when pressed for a centern amount of time
"""
import os
import time
from aiy.vision.leds import RgbLeds
from gpiozero import Button
from gpiozero import LED
from aiy.vision.pins import BUTTON_GPIO_PIN
elapsed_time = 5
button = Button(BUTTON_GPIO_PIN)
leds = Leds()
RED = (0xFF, 0x00, 0x00)
GREEN = (0x00, 0xFF, 0x00)
YELLOW = (0xFF, 0xFF, 0x00)
BLUE = (0x00, 0x00, 0xFF)
PURPLE = (0xFF, 0x00, 0xFF)
CYAN = (0x00, 0xFF, 0xFF)
WHITE = (0xFF, 0xFF, 0xFF)

def shutdown_confirmation():
    print('Breathe RED for 5 seconds')
    start_time_breathe = time.time()
    leds.update(Leds.rgb_pattern(RED))
    while button.is_pressed:
        if( 4 <= time.time() - start_time_breathe ):
                print("Shutting down")
                shutdown_confirmation()
    leds.reset()
    os.system('shutdown now -h')

while True:
    if button.is_pressed:
        start_time = time.time()
        while button.is_pressed:
            time.sleep(0.2)
            if( elapsed_time <= time.time() - start_time ):
                print("Shutting down")
                shutdown_confirmation()
            
            print("Counting...")
    else:
        time.sleep(0.5)
        print("Button is not being pressed")

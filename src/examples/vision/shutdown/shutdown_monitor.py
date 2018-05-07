#!/usr/bin/env python3
"""Monitor the button and perform shutdown 
when pressed for a centern amount of time
"""
import os
import time
import aiy.toneplayer
from aiy.vision.leds import Leds
from aiy.vision.leds import Pattern
from aiy.vision.leds import RgbLeds
from gpiozero import Button
from gpiozero import LED
from aiy.vision.pins import BUTTON_GPIO_PIN
elapsed_time = 5
button = Button(BUTTON_GPIO_PIN)
leds = Leds()
RED = (0xFF, 0x00, 0x00)

def shutdown_confirmation():
    player = aiy.toneplayer.TonePlayer(22)
    print('Breathe RED')
    leds.pattern = Pattern.breathe(1000)
    start_time_breathe = time.time()
    leds.update(Leds.rgb_pattern(RED))
    player.play('E5q','Be','C5e')
    sleep(3)
    # leds.reset()
    os.system('sudo poweroff')

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

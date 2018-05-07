#!/usr/bin/env python3
"""Monitor the button and perform shutdown 
when pressed for a centern amount of time
"""
import os
import time
from signal import pause
from gpiozero import Button
from gpiozero import LED
from aiy.vision.pins import BUTTON_GPIO_PIN
elapsed_time = 5
button = Button(BUTTON_GPIO_PIN)

while True:
    if button.is_pressed:
        start_time = time.time()
        while button.is_pressed:
            sleep(0.2)
            if( elapsed_time >= time.time() - start_time ):
                print(Shutting down)
                sleep(5)
                os.system('shutdown now -h')
    else:
        time.sleep(0.5)

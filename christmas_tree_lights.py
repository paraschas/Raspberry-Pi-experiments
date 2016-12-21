#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dimitrios Paraschas (paraschas@gmail.com)


import time
import sys

import RPi.GPIO as GPIO


def send_high_low(pin, duration=0.5):
    """
    set the pin to high and then to low
    """
    GPIO.output(pin, GPIO.HIGH)
    print("LED on")
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)
    print("LED off")
    time.sleep(duration)


def main():
    """
    main function
    """
    print("blink an LED connected on pin 18 (BCM numbering) for 4 times")
    print("you can also pass the pin number and the number of repetitions as arguments")

    if len(sys.argv) == 3:
        pin = int(sys.argv[1])
        repetitions = int(sys.argv[2])
    else:
        pin = 18
        repetitions = 4

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(pin, GPIO.OUT)

    for _ in range(repetitions):
        send_high_low(pin)

    GPIO.cleanup()


if __name__ == "__main__":
    main()

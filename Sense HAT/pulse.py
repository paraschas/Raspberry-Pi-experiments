#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Dimitrios Paraschas (paraschas@gmail.com)


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.dont_write_bytecode = True

import time

try:
    from sense_hat import SenseHat
except ImportError:
    from sense_emu import SenseHat


def main():
    """
    main function
    """
    # off
    B = [0, 0, 0]
    # full on
    W = [255, 255, 255]
    # half on
    w = [127, 127, 127]
    # red
    R = [255, 0, 0]
    # green
    G = [0, 100, 0]
    # blue
    B = [0, 0, 128]

    sense = SenseHat()

    sense.clear()

    full_on = [W for _ in range(64)]
    half_on = [w for _ in range(64)]

    while True:
        sense.set_pixels(full_on)

        time.sleep(0.2)

        sense.clear()

        time.sleep(1)


if __name__ == "__main__":
    main()

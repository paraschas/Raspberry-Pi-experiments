#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Dimitrios Paraschas (paraschas@gmail.com)


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.dont_write_bytecode = True

import time

from pygame import mixer


def main():
    """
    main function
    """
    print("This program plays the first 5 seconds of an mp3 audio file passed as its argument.")

    mp3_file = sys.argv[1]

    mixer.init()
    mixer.music.load(mp3_file)
    mixer.music.play()

    run_time = 5
    end_time = time.time() + run_time

    while time.time() < end_time and mixer.music.get_busy():
        continue


if __name__ == "__main__":
    main()

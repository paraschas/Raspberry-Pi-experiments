#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Dimitrios Paraschas (paraschas@gmail.com)


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
sys.dont_write_bytecode = True

from sense_hat import SenseHat


def main():
    """
    main function
    """
    sense = SenseHat()

    sense.clear()


if __name__ == "__main__":
    main()

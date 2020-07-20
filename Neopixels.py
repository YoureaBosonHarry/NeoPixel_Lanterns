import board
from flask import Flask
from flask import request
import multiprocessing
import neopixel
import numpy as np
import os
import socket
import time

pixels_per_lantern = 12
number_of_lanterns = 8

pixels = neopixel.NeoPixel(board.D18, pixels_per_lantern*number_of_lanterns, auto_write=False)

class Lantern():
    def __init__(self, start_pixel, end_pixel):
        self.start_pixel = start_pixel
        self.end_pixel = end_pixel

    def clear_lantern(self):
        for i in range(self.start_pixel, self.end_pixel):
            pixels[i] = (0, 0, 0)
        pixels.show()

    def solid_pattern(self, r, g, b):
        for i in range(self.start_pixel, self.end_pixel):
            pixels[i] = (r, g, b)
        pixels.show()

def create_lanterns():
    current_pixel = 0
    lantern = {}
    for i in range(number_of_lanterns):
        lantern[i] = Lantern(current_pixel, current_pixel + pixels_per_lantern)
        current_pixel += pixels_per_lantern
    return lantern

if __name__ == '__main__':
    lanterns = create_lanterns()
    lanterns.solid_pattern()

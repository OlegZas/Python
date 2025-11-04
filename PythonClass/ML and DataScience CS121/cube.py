
from square import Square # importing Point class # will create instances later 
import math

class Cube: 

    def __init__(self, square):
        '''cube with square object'''
        self._SQUARE = square

    def volume(self):
        side = self._SQUARE.length()
        return side ** 3

    def surfacearea(self):
        side = self._SQUARE.length()
        return 6*(side **2)

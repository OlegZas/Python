from point import Point # importing Point class # will create instances later 
import math

class Square:
    '''instances of POINT class above as propreties to create a square'''

    def __init__(self, first, second):
        '''initializing square'''    
        self._FIRST = first # internal attribute of sq
        self._SECOND = second 

    def length(self): #method to calculate the side lenght 
        return abs(self._FIRST._X - self._SECOND._X) #horizontal distance between the two 
# have to use absolute value function otherwise the results are nonsencical down the line 

    def area(self): #now just need to find the area 
        '''Returning area of the square'''
        side = self.length() #calling length method hre 
        return side ** 2

    def perimeter(self):
        side = self.length()
        return 4 * side
import math 

#Phase 1 Points 
class Point: # not sure if i am supposed to change this example. 
    """Oleg's private class initializing Point object"""
    def __init__(self, x, y):

        self._X = x # "ideally coordinates should be x and y" so ill keep as they are 
        self._Y = y #'capitalized since they should be constant and hide them with underscore.' 


    def distance(self, other):
        """Method to find distance from point X to Y"""
        return round(math.sqrt((self._X - other._X)**2 + (self._Y - other._Y)**2),2) # rounding bonus
# s.x - o.x is the change in xaxis ; s.y - o.y change in y axis. 
    #then square and add since sum of a and b squared = c squared (hypothenuse)
    # so we get the sum of squares of horizontal nad vert differences 
    # then sqrt to solve for c - distance (hypotenuse)

    def slope(self, other):
        """Public mehtod to find the slope of the line"""
        return (other._Y - self._Y) / (other._X - self._X)
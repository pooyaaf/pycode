import math
class Point:
    def __init__(self,x:int,y:int) :
        self.x=x
        self.y=y
    def dist(self,point):
        return math.sqrt((self.x-point.x)**2 + (self.y-point.y)**2)
class Circle:
    def __init__(self,center:Point,r:int) :
        self.__center = center
        self.__radius = r
    def area(self):
        return (self.__radius**2)*3.14
    
#    

circle1 = Circle(Point(1,4),2)
print(circle1.area())
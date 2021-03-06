import math
class Point:
    def __init__(self,x:int,y:int) :
        self.x=x
        self.y=y
    def dist(self,point):
        return math.sqrt((self.x-point.x)**2 + (self.y-point.y)**2)
    def __sub__(self,point):
        return Point(self.x-point.x,self.y-point.y)
    def __add__(self,point):
        return Point(self.x+point.x,self.y+point.y)
    def __str__(self):
        return f"({self.x},{self.y})"
class Circle:
    def __init__(self,center:Point,r:int) :
        self.__center = center
        self.__radius = r
    def area(self):
        return (self.__radius**2)*3.14
    
circle1 = Circle(Point(1,4),2)
print(circle1.area())
#
p1=Point(3,4)
p2=Point(12,1)
print(p1+p2)
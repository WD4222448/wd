'''
class rectangle:
    def __init__(self):
        self.width=eval(raw_input('width: '))
        self.height=eval(raw_input('height: '))
    def getarea(self):
        area=self.width*self.height
        print area
    def getperimeter(self):
        perimeter=2*(self.width+self.height)
        print perimeter
if __name__=='__main__':
    rectangle().getarea()
    rectangle().getperimeter()
'''
2.
'''
class account:
    def __init__(self,id=0,balance=100,annuallnterestRate=0):
        self.__id=id
        self.__balance=balance
        self.__annual=annual
    def getmonthlyinterestrate(self):
        self.month = self._annual / 12
        print ("The Monthly Interest Rate is " + str(round(self.month.5)))
    def getmonthlyinterest(self):
        self.monthly = self.__balance * self.month
        print ("The Monthly Interest is"+ str(round(self.monthly.5)))
    def withdraw(self,dollar):
        self._balance -= dollar
    def deposit(self,dollar):
        self._balance += dollar
    def show(self):
        print("id: "+ str(self._id))
        print("balance: "+ str(self._balance))
        self.getmonthlyinterestrate()
        self.getmonthlyinterest()
a = account(1122, 20000,0.045)
a.withdraw(2500)
a.deposit(3000)
a.show()
'''
3.
'
import math
class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=n
        self.__s=side
        self.__x=x
        self.__y=y
    def getPerimeter(self):
        p=self.__n*self.__s
        print('Perimeter:'+str(p))
    def getArea(self):
        a=(self.__n*self.__s**2)/(4*math.tan(math.pi/self.__n))
        print('Area:'+str(a))
print('--------1--------')
RegularPolygon().getPerimeter()
RegularPolygon().getArea()
print('--------2--------')
RegularPolygon(6,4).getPerimeter()
RegularPolygon(6,4).getArea()
print('--------3--------')
RegularPolygon(10,4,5.6,7.8).getPerimeter()
RegularPolygon(10,4,5.6,7.8).getArea()
'''
4.
'''
class Fan:
    SLOW=1
    MEDIUM=2
    FAST=3
    def __init__(self,speed=SLOW,radius=5,color='blue',on=False):
        self.__speed=speed
        self.__on=on
        self.__radius=radius
        self.__color=color
        print('Speed:'+str(self.__speed))
        print('Radius:'+str(self.__radius))
        print('Color:'+str(self.__color))
        print('On:'+str(self.__on))
print('--------1--------')
Fan(Fan.FAST,10,'yellow',True)
print('--------2--------')
Fan(Fan.MEDIUM)'''        
'''
6.
''

import math
class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def isSolvable(self):
        if (self.__a*self.__d-self.__b*self.__c)!=0:
            return True
    def getX(self):
        x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        return x
    def getY(self):
        y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
        return y
a,b,c,d,e,f=eval(raw_input('Enter a,b,c,d,e,f:'))
m=LinearEquation(a,b,c,d,e,f)
if m.isSolvable()!=True:
    print('The equation has no solution')
else:
print('x is '+str(m.getX())+' and '+'y is '+str(m.getY()))
'''
7.
'''
import math
class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def isSolvable(self):
        if (self.__a*self.__d-self.__b*self.__c)!=0:
            return True
    def getX(self):
        x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        return x
    def getY(self):
        y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
        return y
x1,y1,x2,y2=eval(raw_input('Enter the endpoints of the first line segment:'))
x3,y3,x4,y4=eval(raw_input('Enter the endpoints of the second line segment:'))
a=y1-y2
b=x2-x1
e=x2*y1-x1*y2
c=y3-y4
d=x4-x3
f=x4*y3-x3*y4
print(a,b,e,c,d,f)
m=LinearEquation(a,b,c,d,e,f)
if m.isSolvable()!=True:
    print('The equation has on solution')
else:
    print('The intersecting point is:('+str(m.getX())+','+str(m.getY())+')')'''
'''


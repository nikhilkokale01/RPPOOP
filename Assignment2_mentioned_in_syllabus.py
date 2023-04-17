
class Polygon:
    def __init__(self):
        pass
        
class Square(Polygon):
    def setlength(self):
        p=int(input("Enter the length:"))
        
        if(p<=0):
            print("Please enter valid length")
            self.length=p
        
        else:
            self.length=p
        
        
    def getlength(self):
        if(self.length>0):
            print("The length is:",self.length)
            
    def Area(self):
        if(self.length>0):
            area=(self.length)**2
            print("The area of square is:",area)
        
    
        
        
        
    def Perimeter(self):
        if(self.length>0):
            perimeter=4*self.length
            print("The perimeter of square is:",perimeter)
        


class Triangle(Polygon):
    def setlength(self):
        a=int(input("Enter the first side"))
        b=int(input("Enter the second side"))
        c=int(input("Enter the third side"))
        
        self.a=a
        self.b=b
        self.c=c
        
        if((self.a <0) or (self.b <0)or (self.c<0)):
            print("Enter valid lengths")
            
        if(((self.a <0) and (self.b <0) and (self.c<0)) and ((self.a+self.b<=self.c) or (self.a+self.b<=self.c)or (self.a+self.b<=self.c))):
            print("Enter valid combination of lengths such that a+b >c")
        
       
        
    def getlength(self):
        if((self.a>0) and (self.b>0) and (self.c>0) and ((self.a+self.b>self.c) or (self.a+self.b>self.c)or (self.a+self.b>self.c))):
            print("The first side of triangle is of length ",self.a)
            print("The second side of triangle is of length ",self.b)
            print("The third side of triangle is of length ",self.c)
            
            
    def Perimeter(self):
        if((self.a>0) and (self.b>0) and (self.c>0) and ((self.a+self.b>self.c) or (self.a+self.b>self.c)or (self.a+self.b>self.c))):
        
            perimeter=((self.a)+(self.b)+(self.c))/2
            self.perimeter=perimeter
            print("The perimeter of triangle is",perimeter)
            
    def Area(self):
        if((self.a>0) and (self.b>0) and (self.c>0) and ((self.a+self.b>self.c) or (self.a+self.b>self.c)or (self.a+self.b>self.c))):
    
            area=(self.perimeter*(self.perimeter-self.a)*(self.perimeter-self.b)*(self.perimeter-self.c))**0.5
            print("The area of triangle is",area)
            
            
        



class Rectangle(Polygon):
    def setlength(self):
        length=int(input("Enter the length of rectangle"))
        self.length=length
        if(self.length<=0):
            print("Enter valid length")
        
       
        breadth=int(input("Enter the breadth of rectangle"))
        
        self.breadth=breadth
            
        if(self.breadth<=0):
            print("Enter valid breadth")
        
    def getlength(self):
        if(self.length>0 and self.breadth>0):
            print("The length of rectangle is",self.length)
            print("The breadth of rectangle is",self.breadth)
            
    def Perimeter(self):
        if(self.length>0 and self.breadth>0):
            perimeter=2*(self.length+self.breadth)
            print("The perimeter of rectangle is",perimeter)
            
    def Area(self):
        if(self.length>0 and self.breadth>0):
            area=(self.length)*(self.breadth)
            print("The perimeter of rectangle is",area)
            
    
n=int(input("Enter a number such that 1 represents square ,2 represents triangle and 3 represents rectangle"))
if(n==1):
    l=Square()
    l.setlength()
    l.getlength()
    l.Perimeter()
    l.Area()
    
elif(n==2):
    l=Triangle()
    l.setlength()
    l.getlength()
    l.Perimeter()
    l.Area()
    
elif(n==3):
    l=Rectangle()
    l.setlength()
    l.getlength()
    l.Perimeter()
    l.Area()

else:
    print("Please enter number from 1 to 3")


    
            
            
        
            



























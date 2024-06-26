
# This code is part of Python course available on CourseGalaxy.com

class Fraction:
    def __init__(self,nr,dr=1):
        self.nr = nr 
        self.dr = dr
        if self.dr < 0:  
            self.nr *= -1
            self.dr *= -1
        self._reduce()

    def show(self):
        print(f'{self.nr}/{self.dr}')

    def add(self,other):
        if isinstance(other,int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
        f._reduce()
        return f

    def multiply(self,other):
        if isinstance(other,int):
            other = Fraction(other)
        f = Fraction(self.nr * other.nr , self.dr * other.dr)
        f._reduce()
        return f

    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        if h == 0:
            return
        
        self.nr //= h
        self.dr //= h
        
    @staticmethod
    def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s

       

f1 = Fraction(2,3)
f2 = Fraction(3,4)

#f3 = f1+f2

##f3 = f1*f2

f3 = f1.add(f2)
f3.show()

f3 = f1.multiply(f2)

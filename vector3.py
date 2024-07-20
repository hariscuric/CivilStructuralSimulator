import math as m

class vector3:
    def __init__(self, component1 : float = 0, component2 : float = 0, component3 : float = 0) -> None:
        self.X = component1
        self.Y = component2
        self.Z = component3

    def __add__(self, other):
        x = self.X + other.X
        y = self.Y + other.Y
        z = self.Z + other.Z
        return vector3(x,y,z)
    
    def __sub__(self, other):
        x = self.X - other.X
        y = self.Y - other.Y
        z = self.Z - other.Z
        return vector3(x,y,z)

    def __mul__(self, scalar : float):
        x = self.X * scalar
        y = self.Y * scalar
        z = self.Z * scalar
        return vector3(x,y,z)
    
    def abs(self):
        absoluteValue = m.sqrt(self.X**2 + self.Y**2 + self.Z**2)
        return absoluteValue
    
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
        
    def __eq__(self, other) -> bool:
        return self.X==other.X and self.Y==other.Y and self.Z==other.Z
    
    def __str__(self):
        return str([self.X, self.Y, self.Z])
    
    def __repr__(self):
        return str([self.X, self.Y, self.Z])
    





class vector2:
    def __init__(self, component1 : float = 0, component2 : float = 0) -> None:
        self.X = component1
        self.Y = component2

    def __add__(self, other):
        x = self.X + other.X
        y = self.Y + other.Y
        return vector2(x,y)
    
    def __sub__(self, other):
        x = self.X - other.X
        y = self.Y - other.Y
        return vector2(x,y)

    def __mul__(self, scalar : float):
        x = self.X * scalar
        y = self.Y * scalar
        return vector2(x,y)
    
    def abs(self):
        absoluteValue = m.sqrt(self.X**2 + self.Y**2)
        return absoluteValue
    
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
        
    def __eq__(self, other) -> bool:
        return self.X==other.X and self.Y==other.Y
    
    def __str__(self):
        return str([self.X, self.Y])
    
    def __repr__(self):
        return str([self.X, self.Y])
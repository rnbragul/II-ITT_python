
class Rectangle:
   def __init__(self,length,breadth):
      self.length=length
      self.breadth=breadth
   def method(self):
      return ((self.length)*(self.breadth))
rec=Rectangle(10,5)
a=rec.method()
print(a)

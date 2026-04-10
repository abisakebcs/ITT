class Rectangle:
   def __init__(self,length,breadth):
      self.length = length
      self.breadth = breadth
   def area(self):
      print("Length:",self.length)
      print("Breadth:",self.breadth)
      print("Area of Rectangle:",self.length * self.breadth)
R = Rectangle(7,3)
R.area()

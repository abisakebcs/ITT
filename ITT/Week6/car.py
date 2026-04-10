class Car:
   def __init__(self,car_name,car_no):
      self.car_name = car_name
      self.car_no = car_no
   def drive(self):
      print("Vroom")
C = Car("Volkswagan",1234)
C.drive()

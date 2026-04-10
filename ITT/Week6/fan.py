class Fan:
   def __init__(self,Speed = "Medium"):
      self.Speed = Speed
   def status(self):
      print("Status of Fan:",self.Speed)
F1 = Fan()
F1.status()

F2 = Fan("High")
F2.status()

F3 = Fan("Low")
F3.status()

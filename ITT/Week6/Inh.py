class Animal:
   def speak(self):
      print("Tweet")
class Bird(Animal):
   def speak(self):
      print("Chirp")
a = Animal()
a.speak()
b = Bird()
b.speak()

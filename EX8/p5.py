
class Animal:
   def speak(self):
      print("animal speaks")
class Cat(Animal):
   def speak(self):
      print("cat tweets")

animal=Animal()
animal.speak()
cat=Cat()
cat.speak()

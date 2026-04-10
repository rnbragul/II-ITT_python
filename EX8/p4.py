class Fan:
   def __init__(self,speed='Medium'):
      self.speed=speed
   def status(self):
      print(f"fan is in speed {self.speed}")
fan=Fan()
fan.status()

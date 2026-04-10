
class Book:
   def __init__(self,title,author):
      self.title=title
      self.author=author
   def display(self):
      print(f"{self.title} is  written by {self.author}.")

book=Book('delulu','maya')
book.display()

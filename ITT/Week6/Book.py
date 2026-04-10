class Book:
   def __init__(self,Book_Title,Book_Author):
      self.Book_Title = Book_Title
      self.Book_Author = Book_Author
   def display(self):
      print("Book Title:",self.Book_Title)
      print("Book Author:",self.Book_Author)
B = Book("The Leader In You","Dale Carnegie")
B.display()

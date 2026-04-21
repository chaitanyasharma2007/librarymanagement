from utils import books

def addBooks():
    BookName=input("Enter the name of the book:")
    BookName.upper()
    books.append(BookName)
    print(f"Book - {BookName} added succesfully")
    










from utils import books,issuedBooks
def issued_Books():
    if len(books)==0:
        print("No books available ")
    else:
        bookname=input("Enter book name:")
        if bookname in books :
            issuedBooks.append(bookname)
            print(f"book - {bookname} issued succesfully")
        else :
            print("No such book issued!")

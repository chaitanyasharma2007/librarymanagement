from utils import books , issuedBooks
def returnbooks():
    if len(books)==0:
        print("No books available ")
    else:
        bookname=input("Enter book name to be returned:")
        if bookname in books :
            issuedBooks.remove(bookname)
            issuedBooks.append(bookname)
            print(f"book - {bookname} returned succesfully")
        else :
            print("No such book issued!")


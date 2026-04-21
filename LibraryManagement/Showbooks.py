from utils import books

def Showbook():
    if len(books)==0:
        print("No books avaiable!")
    else : 
        for i in books:
            print(i)

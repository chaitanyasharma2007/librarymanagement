from addBooks import addBooks
from Showbooks import Showbook
from returnedBooks import returnbooks
from issuedBooks import issued_Books

def library():
    while True:
        print("\n1. Add books")
        print("\n2. Show books")
        print("\n3. Issues books")
        print("\n4. Return books")
        print("\n5.  Exit")
        choice =input("Enter your choice: ")
        if choice.isdigit(): 
            choice=int(choice)
            if choice == 1 : 
                addBooks()
            elif choice ==2 : 
                Showbook()
            elif choice == 3:
                issued_Books()
            elif choice ==4 :
                returnbooks()
            elif choice==5:
                print("Loggin off!")
                break
            else :
                print("Invalid input")            
    
    
library()
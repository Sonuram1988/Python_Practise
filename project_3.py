class Library:
    def __init__(self,listofBooks):
        self.books=listofBooks
    
    def displayAvailableBooks(self):
        print(f"These books are available:\n")
        for book in self.books:
            print("\t"+"*"+book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"{bookName} is issued.Please keep it safe")
            self.books.remove(bookName)
        else:
            print(f"Sorry,This book is issued to someone.Please wait untill this books is return.")

    def returnBook(self,bookName):
        print(f"Thanks for return this book {bookName}")
        self.books.append(bookName)

class Student:
    def reqBook(self):
        reqBook=input("Enter the name of books which you want to borrow:\n")
        self.reqBook=reqBook
        return self.reqBook
    
    def returnBook(self):
        returnBook=input("Enter the name of book which you want to return:\n")
        self.returnBook=returnBook
        return self.returnBook

l1=Library(["Python","Java Script","Java","Android"])
s1=Student()

while(True):
    welcoMsg='''====Welcome in Central Library===
    Please choose an option:
    1. Listing all the books
    2. Request a book
    3. Return/add book
    4. Exit
    '''
    print(welcoMsg)
    num=int(input("Enter a number:\n"))
    if(num==1):
        l1.displayAvailableBooks()
    elif(num==2):
        l1.borrowBook( s1.reqBook())
    elif(num==3):
        l1.returnBook(s1.returnBook())
    elif(num==4):
        print("Thanks for choosing central library")
        exit()
    else:
        print("Invaild option")




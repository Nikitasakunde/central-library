class Librery:

    def __init__(self,listOfBooks) -> None:
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("the books present in this library are : ")
        for books in self.books:
            print("\t* " + books)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName} book . please keep it safe and return it within 30 days ")

            self.books.remove(bookName)
            return True
        else:
            print("sorry !! this book is either not available or already being issued to someone else. please wait until the book is available")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("thanks for returning this book. hope you like reading it!!")


class Student:
    def requestBook(self):
        self.book = input("enter the name of book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("enter the name of book you want to return: ")
        return self.book



if __name__ == "__main__":
    centraLibreary = Librery(["algorithms" , "Django" , "pyhton notes" , "clrs" , "data structures" , "aplications of discrete mathematics"])
    student = Student()
    centraLibreary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''
        ======= welcome to central lbrary ========
        please choose an option: 
        1. list all books
        2. borrow a book
        3. return a book
        4. exit the library        
        '''
        print(welcomeMsg)
        a = int(input("enter the choice: "))
        if a== 1:
            centraLibreary.displayAvailableBooks()
        elif a == 2:
            centraLibreary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibreary.returnBook(student.returnBook())
        elif a == 4:
            print("thanks for choosing central library!!!")
            exit()
        else:
            print("Invalid Choice!!")
        print(welcomeMsg)


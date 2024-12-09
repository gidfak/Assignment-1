#books
Books = ['Python basics', 'Data sceince 101', 'AI for begineers']

#view availability
def view_books():
    print("Avalable books:")
    if not Books:
        print("Not found")
    else:
        for book in Books:
            print(book)

#borrow book
def borrow_book():
    book_to_borrow = input("Enter the name of the book ")
    if book_to_borrow in Books:
        Books.remove(book_to_borrow)
        print(f"you have sucessfully borrowed '{book_to_borrow}'.")
        

    else:
        print(F" '{ book_to_borrow}' is not available.")


#returnbook
def return_book():
    Book_to_return = input(" Enter the name of the book you want to return")
    Books.append( Book_to_return)
    print(f"Books has been returned succesfully")

#user action
def libary():
    while True:
        print("\n menu:")
        print("1. View available books")
        print("2. Borrow book")
        print("3. Return book")
        print("4. exit")

        Choice = input( " enter your choice (1/2/3/4):")

        if Choice == '1':
            view_books()
        elif Choice == '2':
            borrow_book()
        elif Choice == '3':
            return_book()
        elif Choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid please try again")

libary()      
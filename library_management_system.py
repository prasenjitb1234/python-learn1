class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def view_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("Book ID\tTitle\t\tAuthor\t\tAvailability")
        for book_id, book in self.books.items():
            availability = "Available" if book.is_available else "Not Available"
            print(f"{book_id}\t{book.title}\t{book.author}\t{availability}")

    def borrow_book(self, book_id):
        book = self.books.get(book_id)
        if book:
            if book.is_available:
                book.is_available = False
                print(f"You have borrowed '{book.title}'. Enjoy reading!")
            else:
                print("Sorry, the book is already borrowed.")
        else:
            print("Book not found in the library.")

    def return_book(self, book_id):
        book = self.books.get(book_id)
        if book:
            if not book.is_available:
                book.is_available = True
                print(f"Thank you for returning '{book.title}'.")
            else:
                print("This book is already in the library.")
        else:
            print("Book not found in the library.")

def display_menu():
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. View all books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")

if __name__ == "__main__":
    library = Library()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            new_book = Book(book_id, title, author)
            library.add_book(new_book)
            print(f"'{title}' by {author} added to the library.")

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            book_id = input("Enter the Book ID to borrow: ")
            library.borrow_book(book_id)

        elif choice == '4':
            book_id = input("Enter the Book ID to return: ")
            library.return_book(book_id)

        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-5).")

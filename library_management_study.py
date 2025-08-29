import json


class Library:
    def __init__(self, library_file, name):
        """Initialize a Library instance with JSON file (to save data) and a name"""
        self.name = name
        self.library_file = library_file
        self.books_list = []  # stores all available books
        self.loans_dict = {}  # stores which user has borrowed each book

        self.load_library()  # load existing data from JSON file

    def normalize_book(self, book):
        """Return normalized version of book title (trim + lowercase)"""
        return book.strip().lower()

    def validate_book_title(self, book):
        """Validate that title is not empty; return stripped version"""
        book = book.strip()
        if not book:
            print("Book title cannot be empty.")
            return None
        return book

    def find_book_in_list(self, book_title, book_list):
        """Find a book in a list by comparing normalized titles"""
        book_normalized = self.normalize_book(book_title)
        for existing_book in book_list:
            if self.normalize_book(existing_book) == book_normalized:
                return existing_book
        return None

    def load_library(self):
        """Load books and loans from JSON file (or start empty if file not found)"""
        try:
            with open(self.library_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books_list = data.get("books", [])
                self.loans_dict = data.get("loans", {})
        except FileNotFoundError:
            self.books_list = []
            self.loans_dict = {}

    def save_library(self):
        """Save current state (books + loans) into JSON file"""
        data = {"books": self.books_list, "loans": self.loans_dict}
        with open(self.library_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def display_books(self):
        """Print all books in the library"""
        if not self.books_list:
            print("No books available in the library.")
            return
        print("Books in the library:")
        for i, book in enumerate(self.books_list, 1):
            print(f"{i}. {book}")

    def display_loans(self):
        """Print all currently loaned books with borrower names"""
        if not self.loans_dict:
            print("No books are currently on loan.")
            return
        print("Currently loaned books:")
        for i, (book, user) in enumerate(self.loans_dict.items(), 1):
            print(f"{i}. {book} is borrowed by {user}")

    def add_book(self, book):
        """Add a new book to the library if it does not already exist"""
        book = self.validate_book_title(book)
        if not book:
            return

        if self.find_book_in_list(book, self.books_list):
            print("Book already exists in the library.")
            return

        self.books_list.append(book)
        self.save_library()
        print(f"Book '{book}' has been added successfully.")

    def delete_book(self, book):
        """Delete a book if it exists and is not currently loaned out"""
        book = self.validate_book_title(book)
        if not book:
            return

        book_to_delete = self.find_book_in_list(book, self.books_list)

        if book_to_delete is None:
            print("Book not found in the library.")
            return

        if book_to_delete in self.loans_dict:
            print("Cannot delete book - it is currently on loan.")
            return

        self.books_list.remove(book_to_delete)
        self.save_library()
        print(f"Book '{book}' has been deleted successfully.")

    def lend_book(self, book):
        """Lend a book to a user"""
        book = self.validate_book_title(book)
        if not book:
            return

        # check if book exists in the library
        book_to_lend = self.find_book_in_list(book, self.books_list)

        if book_to_lend is None:
            print("Sorry! We don't have this book in our library.")
            return

        # check if book is already on loan
        if book_to_lend in self.loans_dict:
            print(f"Book is currently being used by {self.loans_dict[book_to_lend]}")
            return

        # ask for borrower's name
        user = input("Enter the borrower's name: ").strip()
        if not user:
            print("Borrower's name cannot be empty.")
            return

        self.loans_dict[book_to_lend] = user
        self.save_library()
        print(f"Book '{book}' has been loaned to {user}.")

    def return_book(self, book):
        """Return a book (remove it from the loan records)"""
        book = self.validate_book_title(book)
        if not book:
            return

        book_to_return = self.find_book_in_list(book, self.loans_dict.keys())

        if book_to_return is not None:
            self.loans_dict.pop(book_to_return)
            self.save_library()
            print(f"Book '{book}' has been returned.")
        else:
            print("This book is not in the loan records.")


def select_library():
    """Allow user to select which library JSON file to use"""
    city_library = Library("city_library.json", "City Library")
    university_library = Library("university_library.json", "University Library")
    school_library = Library("school_library.json", "School Library")

    libraries = {
        1: city_library,
        2: university_library,
        3: school_library,
    }

    print("=== LIBRARY MANAGEMENT SYSTEM ===")
    print("Select a library:")
    print("1. City Library")
    print("2. University Library")
    print("3. School Library")

    while True:
        try:
            choice = int(input("\nEnter library number (1-3): "))
            if choice in libraries:
                return libraries[choice]
            else:
                print("Please enter a valid number (1-3).")
        except ValueError:
            print("Please enter a valid number.")


def main(library):
    """Main menu loop for interacting with the library"""
    print(f"\n=== WELCOME TO {library.name.upper()} ===")

    while True:
        print(f"\nOptions for {library.name}:")
        print("1. Display all books")
        print("2. Display loaned books")
        print("3. Lend a book")
        print("4. Return a book")
        print("5. Add a book")
        print("6. Delete a book")
        print("7. Change library")
        print("0. Exit program")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                library.display_books()

            elif choice == 2:
                library.display_loans()

            elif choice == 3:
                book = input("Enter the book title to lend: ")
                library.lend_book(book)

            elif choice == 4:
                book = input("Enter the book title to return: ")
                library.return_book(book)

            elif choice == 5:
                book = input("Enter the book title to add: ")
                library.add_book(book)

            elif choice == 6:
                book = input("Enter the book title to delete: ")
                library.delete_book(book)

            elif choice == 7:
                print("\nChanging library...")
                return "change_library"

            elif choice == 0:
                print("\nGoodbye!")
                return "exit"

            else:
                print("Please choose a valid option (0-7).")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    """Entry point: allow user to select a library and start the menu"""
    while True:
        selected_library = select_library()
        result = main(selected_library)

        if result == "exit":
            break
        elif result == "change_library":
            continue

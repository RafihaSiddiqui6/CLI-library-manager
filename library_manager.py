import os
import csv

# File to store books
books_file = "library.txt"

# Function to load books from file
def load_books():
    books = []
    if os.path.exists(books_file):
        with open(books_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert string to boolean for read status
                row['Read Status'] = row['Read Status'] == 'True'
                # Convert year to integer
                row['Year'] = int(row['Year'])
                books.append(row)
    return books

# Function to save books to file
def save_books(books):
    with open(books_file, 'w', newline='') as file:
        if books:
            writer = csv.DictWriter(file, fieldnames=books[0].keys())
            writer.writeheader()
            writer.writerows(books)
        else:
            writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Genre", "Year", "Read Status"])
            writer.writeheader()
    print("Books saved to file!")

# Function to add a book
def add_book(books):
    print("\nAdd a New Book")
    title = input("Book Title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    
    # Get year with simple validation
    year = 0
    while year < 1000 or year > 2025:
        try:
            year = int(input("Publication Year (1000-2025): "))
        except:
            print("Please enter a valid year!")
    
    # Get read status
    read_input = input("Have you read this book? (yes/no): ")
    read_status = read_input.lower() in ['yes', 'y']
    
    # Create and add the book
    book = {
        "Title": title,
        "Author": author,
        "Genre": genre,
        "Year": year,
        "Read Status": read_status
    }
    books.append(book)
    print("Book added!")

# Function to remove a book
def remove_book(books):
    if not books:
        print("Your library is empty!")
        return
    
    print("\nRemove a Book")
    title = input("Enter book title to remove: ")
    
    for i in range(len(books)):
        if books[i]["Title"].lower() == title.lower():
            del books[i]
            print("Book removed!")
            return
    
    print("Book not found!")

# Function to search for books
def search_books(books):
    if not books:
        print("Your library is empty!")
        return
    
    print("\nSearch Books")
    print("1. Search by Title")
    print("2. Search by Author")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == '1':
        search_term = input("Enter title: ")
        field = "Title"
    elif choice == '2':
        search_term = input("Enter author: ")
        field = "Author"
    else:
        print("Invalid choice!")
        return
    
    found = False
    for book in books:
        if search_term.lower() in book[field].lower():
            if not found:
                print("\nMatching Books:")
                found = True
            print(f"- {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read Status'] else 'Unread'}")
    
    if not found:
        print("No books found!")

# Function to display all books
def display_books(books):
    if not books:
        print("Your library is empty!")
        return
    
    print("\nYour Library:")
    for i, book in enumerate(books, 1):
        status = "Read" if book["Read Status"] else "Unread"
        print(f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {status}")

# Function to display statistics
def display_stats(books):
    total = len(books)
    read = sum(1 for book in books if book["Read Status"])
    percent = (read / total * 100) if total > 0 else 0
    
    print("\nLibrary Statistics:")
    print(f"Total books: {total}")
    print(f"Books read: {read} out of {total} ({percent:.1f}%)")

# Main function
def main():
    books = load_books()
    
    while True:
        print("\n--- Personal Library Manager ---")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_book(books)
            save_books(books)
        elif choice == '2':
            remove_book(books)
            save_books(books)
        elif choice == '3':
            search_books(books)
        elif choice == '4':
            display_books(books)
        elif choice == '5':
            display_stats(books)
        elif choice == '6':
            save_books(books)
            print("Congrats!")
            break
        else:
            print("Invalid choice! Try again.")

# Run the program
if __name__ == "__main__":
    main()

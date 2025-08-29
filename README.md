# Library Management System (Study Example)

This is a simple Python study project that demonstrates basic programming concepts such as classes, methods, lists, dictionaries, user input, and working with JSON files. This project is a command-line interface (CLI) application.

The program simulates a small Library Management System, where a user can:
- Display all available books
- Display all loaned books
- Lend a book to a user
- Return a book
- Add a new book
- Delete a book
- Switch between different libraries

## Project Structure
- `library_management_study.py` → main library code
- `city_library.json` → example JSON data for City Library
- `university_library.json` → example JSON data for University Library
- `school_library.json` → example JSON data for School Library

## Requirements
- Python 3 or higher  
(No external packages are required – only standard library modules are used.)

## How to Run
Run the main program:

### Windows
```bash
python library_management_study.py
```

### macOS / Linux
```bash
python3 library_management_study.py
```

## Notes
- This project uses relative paths for JSON files. Run the script from the same folder where the `.py` file and the `.json` files are located. If you move the project to another folder, move the `.py` and `.json` files together.
- JSON files are automatically updated when books are added, deleted, loaned, or returned.
- If a JSON file does not exist, it will be created automatically.
- This is a study project intended for learning and sharing with students.

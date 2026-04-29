# Library Management CLI

A simple Python command-line application for managing small library collections.

This project was created as a study project to practice core Python concepts such as classes, methods, lists, dictionaries, user input, file handling, and working with JSON data.

## Features

- Display all books in a library
- Display currently loaned books
- Lend a book to a user
- Return a borrowed book
- Add a new book
- Delete a book
- Switch between multiple libraries

## Project Structure

- `library_management_cli.py` - main application file
- `city_library.json` - sample data for City Library
- `university_library.json` - sample data for University Library
- `school_library.json` - sample data for School Library

## Requirements

- Python 3

No external packages are required. The project only uses Python's standard library.

## How to Run

Windows:

```bash
python library_management_cli.py
```

macOS / Linux:

```bash
python3 library_management_cli.py
```

## Notes

- Run the program from the project folder so it can access the JSON files.
- JSON files are updated when books are added, deleted, loaned, or returned.
- If a JSON file is missing, the program starts with an empty library and creates the file when data is saved.
- This project is intentionally simple and focuses on basic Python and CLI logic.

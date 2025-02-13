# Phonebook Directory Program

This Python program implements a simple phonebook directory, allowing users to store, search, and delete contact information.

## Description

The `a_phonebook_directory_system_using_python.py` script provides a command-line interface for managing contacts.  It stores contact details (name, phone number, email) in a text file named `myphonebookfile.txt`. The program offers the following functionalities:

*   **Show All Contacts:** Displays all contacts currently stored in the phonebook.
*   **Add New Contact:**  Adds a new contact to the phonebook, prompting the user for first name, last name, phone number, and email address.
*   **Delete a Contact:** Deletes a specific contact from the phonebook based on the contact's name.
*   **Search a Contact:** Searches for a contact by first name and displays the contact details.
*   **Exit:** Exits the phonebook program.

The program uses file handling to store and retrieve contact information and functions to organize the code.  Lambda functions are used for capitalizing names.

## How to Use

1.  **Clone the Repository (if applicable):**

    ```bash
    git clone https://github.com/kunal430/python-projects.git
    ```

2.  **Run the Script:**

    ```bash
    a_phonebook_directory_system_using_python.py
    ```

3.  **Use the Menu:** The program will display a menu with the available options.  Enter the number corresponding to your desired action.

4.  **Follow the Prompts:** The program will guide you through the process of adding, deleting, or searching for contacts.

5.  **View the Results:**  The program will display the requested information or appropriate messages.

## Code Explanation

The code is organized into several functions:

*   **`search_contact()`:** Searches for a contact by first name.
*   **`capitalize_first_letter()` (lambda):** Capitalizes the first letter of a name.
*   **`input_first_name()`:** Gets the first name from the user.
*   **`input_last_name()`:** Gets the last name from the user.
*   **`new_contact()`:** Adds a new contact to the phonebook file.
*   **`delete_contact()`:** Deletes a contact from the file.
*   **`main()`:** The main function that displays the menu and controls the program flow.

The program uses file I/O to read and write contact information to `myphonebookfile.txt`.  The `with open(...)` context manager ensures that files are properly closed.

## Learnings

This project helped me learn and practice:

*   **File Handling:** Reading and writing to text files.
*   **Functions:** Defining and calling functions to structure code.
*   **Lambda Functions:** Using lambda functions for concise operations.
*   **String Manipulation:** Working with strings, including capitalization.
*   **User Input:** Taking input from the user.
*   **Control Flow (Loops and Conditionals):** Using `while` loops and `if/elif/else` statements.
*   **Data Storage:**  Storing data persistently in a file.

## Contributing

Contributions are welcome! Please submit pull requests for any bug fixes, improvements, or new features.

## License

[Choose a License - e.g., MIT License]
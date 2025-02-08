# Simple Calculator Program

This Python project implements a simple calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division) and calculates the perimeter and area of common geometric shapes.

## Description

The `calculator.py` script provides a menu-driven interface for performing calculations.  It offers the following functionalities:

*   **Simple Calculator:** Performs addition, subtraction, multiplication, and division on two user-provided numbers.
*   **Perimeter Calculator:** Calculates the perimeter of a circle, rectangle, or square based on user-provided dimensions.
*   **Area Calculator:** Calculates the area of a circle, rectangle, or square based on user-provided dimensions.

The program uses functions (including lambda functions for brevity) to perform the calculations and a `while` loop to present the main menu to the user. Input validation is included to handle some common user errors (e.g., incorrect input).

## How to Use

1.  **Clone the Repository (if applicable):**  If you're accessing this project from a repository (e.g., GitHub), clone it:

    ```bash
    git clone https://github.com/kunal430/python-projects.git
    ```

2.  **Run the Script:** Navigate to the project directory in your terminal and execute the Python script:

    ```bash
    a_calculation_system_using_python_.py
    ```

3.  **Use the Menu:** The program will display a menu with the following options:

    *   1. Simple Calculator
    *   2. Perimeter Calculator
    *   3. Area Calculator
    *   4. Exit

4.  **Select an Option:** Enter the number corresponding to the desired calculation type.

5.  **Follow the Prompts:** The program will prompt you to enter the necessary numbers or dimensions.

6.  **View the Result:** The calculated result will be displayed.

7.  **Exit:** To exit the program, choose option 4 from the main menu.

## Code Explanation

The code is structured as follows:

*   **Functions for Calculations:**  Separate functions are defined for each calculation: `add()`, `sub()`, `mul()`, `div()`, `p_circle()`, `p_rectangle()`, `p_square()`, `a_circle()`, `a_rectangle()`, `a_square()`.  Lambda functions are used for the perimeter and area calculations for conciseness.
*   **Main Loop and Menu:** A `while True` loop creates the main menu and handles user input.
*   **Conditional Logic:** `if`, `elif`, and `else` statements are used to direct the program flow based on user choices.
*   **Input Handling:** The `input()` function is used to get user input, and basic type conversion (`int()`, `float()`) is performed.

## Contributing

Contributions are welcome! Please submit pull requests for any bug fixes, improvements, or new features.

## License

[Choose a License - e.g., MIT License]
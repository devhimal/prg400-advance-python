# OOP Concepts in Python

This project demonstrates basic Object-Oriented Programming (OOP) concepts using a simple Python script.

## Concepts Demonstrated

*   **Encapsulation**: The `Employee` class encapsulates the attributes `_name`, `_age`, and `__salary`. Access to these attributes is controlled through getter and setter methods.
*   **Inheritance**: The `Developer` and `Manager` classes inherit from the `Employee` class, reusing its attributes and methods.
*   **Polymorphism**: The `work` method is overridden in the `Developer` and `Manager` classes to provide specific implementations for each type of employee.

## Classes

### `Employee` (Base Class)

This is the base class that represents a generic employee.

*   **Attributes**:
    *   `_name` (protected): The employee's name.
    *   `_age` (protected): The employee's age.
    *   `__salary` (private): The employee's salary.
*   **Methods**:
    *   `set_name(name)`: Sets the employee's name.
    *   `get_name()`: Returns the employee's name.
    *   `set_age(age)`: Sets the employee's age.
    *   `get_age()`: Returns the employee's age.
    *   `set_salary(salary)`: Sets the employee's salary.
    *   `get_salary()`: Returns the employee's salary.
    *   `work()`: Prints a generic work message.

### `Developer` (Derived Class)

This class represents a developer, inheriting from `Employee`.

*   **Attributes**:
    *   `programming_language`: The programming language the developer uses.
*   **Methods**:
    *   `work()`: Overrides the base class method to print a developer-specific work message.
    *   `debug()`: Prints a message indicating the developer is debugging.

### `Manager` (Derived Class)

This class represents a manager, inheriting from `Employee`.

*   **Attributes**:
    *   `team_size`: The size of the team the manager leads.
*   **Methods**:
    *   `work()`: Overrides the base class method to print a manager-specific work message.

## How to Run

1.  Make sure you have Python installed.
2.  Save the code as a Python file (e.g., `week1.py`).
3.  Run the script from your terminal:

```bash
python week1.py
```
Output file 

<img width="1362" height="571" alt="Screenshot from 2025-11-02 18-29-30" src="https://github.com/user-attachments/assets/7e7e27a5-d628-492a-bb9e-d91492b81197" />


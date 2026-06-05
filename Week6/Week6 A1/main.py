from users import (        # Used import function to import the functions from users.py file
    student_login,
    submit_assignment,
    view_grades
)


def main():   # Defined the main function to call the functions from users.py file

    student_login("Mohammad")

    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    view_grades("Alex")


if __name__ == "__main__": # This condition checks if the script is being run directly (as the main program) rather than imported as a module. If this condition is true, it calls the main() function to execute the program.
    main()

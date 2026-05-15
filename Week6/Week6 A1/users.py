from decorators import log_activity # This line imports the log_activity decorator from the decorators.py file. The log_activity decorator is used to log the activity of the functions in this file, such as when a student logs in, submits an assignment, or views grades.


@log_activity # This is a decorator that wraps the submit_assignment function. It will log the activity of the function, including the function name and the time it was called.
def student_login(username):
    print(f"{username} logged into the system.")


@log_activity # This is a decorator that wraps the submit_assignment function. It will log the activity of the function, including the function name and the time it was called.
def submit_assignment(username, assignment):
    print(f"{username} submitted {assignment}.")


@log_activity # This is a decorator that wraps the view_grades function. It will log the activity of the function, including the function name and the time it was called.
def view_grades(username):
    print(f"{username} is viewing grades.")

from datetime import datetime



def log_activity(func):

    def wrapper(*args, **kwargs): # This is a wrapper function that takes any number of positional and keyword arguments. It allows the decorator to work with functions that have different signatures.
        print("===================================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}") 
        print("Activity started...")

        result = func(*args, **kwargs)

        print("Activity completed.")
        print("===================================\n")

        return result

    return wrapper

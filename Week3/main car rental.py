# Welcome to YBS Care rental Services

from database import create_table                                       # table creation
from user_manager import add_customer, add_email, search_user, delete_user # create a your own user_manager name it as register

def menu():
    print("\n==== Customer Registration ====")
    print("Surname:")
    print("Given name:")
    print("Email")
    print("Address")
    print("Birthday") # calculate age
    print("Regular customer")
    print("Login")
    print("Password")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_customer(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

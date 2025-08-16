import os

FILE_NAME = "contacts.txt"

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    try:
        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{phone}\n")
        print("Contact added successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")

def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.")
                return
            print("\nAll Contacts:")
            for contact in contacts:
                name, phone = contact.strip().split(",")
                print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("No contacts file found. Add a contact first.")
    except Exception as e:
        print(f"Error reading file: {e}")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    try:
        with open(FILE_NAME, "r") as file:
            for contact in file:
                name, phone = contact.strip().split(",")
                if search_name in name.lower():
                    print(f"Found: Name: {name}, Phone: {phone}")
                    found = True
        if not found:
            print("No contact found with that name.")
    except FileNotFoundError:
        print("No contacts file found. Add a contact first.")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()

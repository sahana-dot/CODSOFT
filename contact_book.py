def display_menu():
    print("\n==============================")
    print("        CONTACT BOOK")
    print("==============================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name.lower()] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for contact in contacts.values():
        print(f"Name: {contact['name']} | Phone: {contact['phone']}")


def search_contact(contacts):
    search = input("Enter name or phone to search: ").lower()

    found = False
    for contact in contacts.values():
        if search in contact["name"].lower() or search in contact["phone"]:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True

    if not found:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter name of contact to update: ").lower()

    if name in contacts:
        print("Leave blank to keep old value.")

        phone = input("New Phone: ")
        email = input("New Email: ")
        address = input("New Address: ")

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address

        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter name of contact to delete: ").lower()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def main():
    contacts = {}

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
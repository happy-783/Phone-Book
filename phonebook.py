class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"


contacts = []
contact_dict = {}


def add_contact(name, phone):
    c = Contact(name, phone)
    contacts.append(c)
    contact_dict[name.lower()] = c


def view_contact():
    if not contacts:
        print("No contacts available.")
    else:
        for c in contacts:
            print(c)


def edit_contact(name, new_phone):
    if name.lower() in contact_dict:
        contact_dict[name.lower()].phone = new_phone
        print("Contact updated.")
    else:
        print("Contact not found.")


def delete_contact(name):
    contact = contact_dict.pop(name.lower(), None)
    if contact:
        contacts.remove(contact)
        print("Contact deleted.")
    else:
        print("Contact not found.")


def sort_contact(contact_list):
    n = len(contact_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if contact_list[j].name.lower() > contact_list[j + 1].name.lower():
                contact_list[j], contact_list[j + 1] = contact_list[j + 1], contact_list[j]


def linear_search(contact_list, name):
    for contact in contact_list:
        if contact.name.lower() == name.lower():
            return contact
    return None


def binary_search(contact_list, name):
    sort_contact(contact_list)
    left, right = 0, len(contact_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if contact_list[mid].name.lower() == name.lower():
            return contact_list[mid]
        elif contact_list[mid].name.lower() < name.lower():
            left = mid + 1
        else:
            right = mid - 1
    return None


class Node:
    def __init__(self, contact):
        self.contact = contact
        self.next = None


class ContactLinkedList:
    def __init__(self):
        self.start = None

    def add_contact(self, contact):
        n = Node(contact)
        n.next = self.start
        self.start = n

    def disp_contact(self):
        curr = self.start
        if not curr:
            print("Linked list is empty.")
            return
        while curr:
            print(curr.contact)
            curr = curr.next


def menu():
    while True:
        print("\n--- Contact Management ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Linear Search")
        print("6. Binary Search")
        print("7. Display Contacts via Linked List")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            add_contact(name, phone)
            print("Contact added.")

        elif choice == "2":
            print("\nAll Contacts:")
            view_contact()

        elif choice == "3":
            name = input("Enter name to edit: ")
            new_phone = input("Enter new phone: ")
            edit_contact(name, new_phone)

        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == "5":
            name = input("Enter name to search (linear): ")
            result = linear_search(contacts, name)
            print(result if result else "Not found.")

        elif choice == "6":
            name = input("Enter name to search (binary): ")
            result = binary_search(contacts, name)
            print(result if result else "Not found.")

        elif choice == "7":
            print("Contacts via Linked List:")
            ll = ContactLinkedList()
            for c in contacts:
                ll.add_contact(c)
            ll.disp_contact()

        elif choice == "8":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()

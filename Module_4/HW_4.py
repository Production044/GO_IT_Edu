def parse_input(user_input):
    cmd, *args = user_input.split(maxsplit=2)
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid number of arguments for 'add' command.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid number of arguments for 'change' command.")
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_contact(args, contacts):
    if len(args) != 1:
        raise ValueError("Invalid number of arguments for 'show' command.")
    name, *_ = args
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        return '\n'.join([f"{name}: {phone_number}" for name, phone_number in contacts.items()])
    else:
        return "No contacts saved."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            try:
                print(add_contact(args, contacts))
            except ValueError as e:
                print(e)

        elif command == "change":
            try:
                print(change_contact(args, contacts))
            except ValueError as e:
                print(e)

        elif command == "show":
            try:
                print(show_contact(args, contacts))
            except ValueError as e:
                print(e)

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


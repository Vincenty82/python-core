EXIT_COMMANDS = ["good bye", "close", "exit", "."]
COMMANDS_WITH_SPACE = ["show", "good"]
EXISTING_COMMANDS = ["hello", "add", "edit","phone", "show all", "good bye", "close", "exit", "."]

def input_error(func):
    def friendly_error_message(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as raised_exception:
            if isinstance(raised_exception, ValueError) and str(raised_exception) == "handle_cmd_add_contact_exists":
                return f"ADD >> The contact you are trying to add already exists."
            elif isinstance(raised_exception, TypeError) and str(raised_exception) == "handle_cmd_add() missing 2 required positional arguments: 'contact_name' and 'phone_number'":
                return f"ADD >> When using ADD command, you need to provide both a name and a phone number to get a result."
            elif isinstance(raised_exception, TypeError) and str(raised_exception) == "handle_cmd_add() missing 1 required positional argument: 'phone_number'":
                return f"ADD >> Thanks for providing the name, but you are still required to provide phone number as part of the command."
            elif isinstance(raised_exception, TypeError) and str(raised_exception) == "handle_cmd_edit() missing 2 required positional arguments: 'contact_name' and 'new_phone_number'":
                return f"EDIT >> When using EDIT command, you need to provide both a name and a replacement phone number to get a result."
            elif isinstance(raised_exception, TypeError) and str(raised_exception) == "handle_cmd_edit() missing 1 required positional argument: 'new_phone_number'":
                return f"EDIT >> Thanks for providing the name, but you are still required to provide a replacement phone number as part of the command."
            elif isinstance(raised_exception, TypeError) and str(raised_exception) == "handle_cmd_phone() missing 1 required positional argument: 'contact_name'":
                return f"PHONE >> When you are using PHONE command, you need to provide a name with it to get a result."
            elif isinstance(raised_exception, KeyError):
                return f"LOOK UP >> User does not seem to exist. Remember that contacts are case sensitive.\nIf you are not sure, you can always use \"show all\" command to find the right name."
            else:
                return f"UKNOWN ERROR >> {type(raised_exception).__name__}: {str(raised_exception)}\nCONGRATULATIONS! I did not know this was possible. :)"
    return friendly_error_message

def return_bot_version():
    bot_version = "Assist Bot 2 - version 0.1"
    return bot_version

def parse_command(user_input):
    parsed_input = user_input.split()
    if len(parsed_input) >= 2 and parsed_input[0].lower() in COMMANDS_WITH_SPACE:
        parsed_input[0] = " ".join(parsed_input[:2])
        parsed_input.pop(1)
    return parsed_input

def handle_cmd_hello():
    return "\nHow can I help you?"

@input_error
def handle_cmd_add(contacts_dictionary, contact_name, phone_number):
    if contact_name in contacts_dictionary:
        raise ValueError("handle_cmd_add_contact_exists")
    contacts_dictionary[contact_name] = phone_number
    contact_added_string = f"\n{contact_name} was saved with phone number {phone_number}."
    return contact_added_string

@input_error
def handle_cmd_edit(contacts_dictionary, contact_name, new_phone_number):
    old_phone_number = contacts_dictionary[contact_name]
    contacts_dictionary[contact_name] = new_phone_number
    contact_edited_string = f"\nPhone number for {contact_name} was changed from {old_phone_number} to {new_phone_number}."
    return contact_edited_string

@input_error
def handle_cmd_phone(contacts_dictionary, contact_name):
    phone_number = contacts_dictionary[contact_name]
    contact_phone_string = f"\nPhone number for {contact_name} is {phone_number}."
    return contact_phone_string

def handle_cmd_show_all(contacts_dictionary):
    contacts_with_phones_list = []
    for name_string, phone_string in contacts_dictionary.items():
        contacts_with_phones_list.append(f"{name_string}: {phone_string}")
        show_all_string = "\n" + "\n".join(contacts_with_phones_list)
    return show_all_string

def handle_cmd_exit():
    return "\n" + "Good bye!".center(50) + "\n"

def main():

    contacts_dictionary = {
    "Beata": "506456245",
    "Joanna": "602167448",
    "Alicja": "700345788",
    "Piotr": "502446239",
    "Andrzej": "601887990",
    }

    print("\n" + return_bot_version().center(50))

    while True:

        user_input = input("\nEnter command:")

        if user_input:
            parsed_command, *arguments_list = parse_command(user_input)
        else:
            parsed_command = ""

        if parsed_command.lower() == "hello":
            print(handle_cmd_hello())
        elif parsed_command.lower() == "add":
            print(handle_cmd_add(contacts_dictionary, *arguments_list[:2]))
        elif parsed_command.lower() == "edit":
            print(handle_cmd_edit(contacts_dictionary, *arguments_list[:2]))
        elif parsed_command.lower() == "phone":
            print(handle_cmd_phone(contacts_dictionary, *arguments_list[:1]))
        elif parsed_command.lower() == "show all":
            print(handle_cmd_show_all(contacts_dictionary))
        elif parsed_command.lower() in EXIT_COMMANDS:
            print(handle_cmd_exit())
            break
        else:
            print(f"Command \"{parsed_command}\" was not recognized.\nTry using one of these >> {', '.join(EXISTING_COMMANDS)}")

if __name__ == "__main__":
    main()

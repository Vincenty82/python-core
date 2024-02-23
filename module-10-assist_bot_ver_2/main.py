from collections import UserDict

EXIT_COMMANDS = ["good bye", "close", "exit", "."]
COMMANDS_WITH_SPACE = ["show", "good"]
EXISTING_COMMANDS = ["hello", "add", "edit", "search", "delete", "show all", "good bye", "close", "exit", "."]

class Field:
    pass

class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, number):
        self.number = number

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        for num in self.phones:
            if num.number == phone:
                self.phones.remove(num)
                return
        raise ValueError("Record-remove_phone=does_not_exist")

    def edit_phone(self, old_phone, new_pnone):
        for phone in self.phones:
            if phone.number == old_phone:
                phone.number = new_pnone
                return
        raise ValueError("Record-edit_phone=does_not_exist")

class AddressBook(UserDict):    
    def add_record(self, record):
        self.data[record.name] = record

    def remove_record(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("AdressBook-remove_record=does_not_exist")

    def search_records(self, search_phrase: str):
        results = []
        for name, record in self.data.items():
            if search_phrase in name.value.lower():
                results.append(record)
        if not results:
            raise ValueError("AddressBook-search_records=does_not_exist")
        return results

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
            elif isinstance(raised_exception, ValueError) and str(raised_exception) == "Record-edit_phone=does_not_exist":
                return f"EDIT >> Phone number does not exist. If you want to add a new one, please use ADD command."
            elif isinstance(raised_exception, ValueError) and str(raised_exception) == "AddressBook-search_records=does_not_exist":
                return f"SEARCH >> Name not found."
            elif isinstance(raised_exception, ValueError) and str(raised_exception) == "Record-remove_phone=does_not_exist":
                return f"EDIT >> The phone number you are trying to remove does not exist."
            elif isinstance(raised_exception, KeyError):
                return f"LOOKUP >> Contact does not seem to exist. Make sure you use full name.\nIf you are not sure, you can always use \"search\" or \"show all\" command to find the right contact."
            elif isinstance(raised_exception, UnboundLocalError):
                return f"LOOKUP >> Contact does not seem to exist. Make sure you use full name.\nIf you are not sure, you can always use \"search\" or \"show all\" command to find the right contact."
            else:
                return f"UKNOWN ERROR >> {type(raised_exception).__name__}: {str(raised_exception)}\nCONGRATULATIONS! I did not know this was possible. :)"
    return friendly_error_message

def return_bot_version():
    bot_version = "Assist Bot 2 - version 1.0"
    return bot_version

def initialize_address_book(contacts_data_set: dict):
    initialized_address_book = AddressBook()
    for contact_name, phone_numbers in contacts_data_set.items():
        record = Record(Name(contact_name))
        for phone_number in phone_numbers:
            record.add_phone(Phone(phone_number))
        initialized_address_book.add_record(record)
    return initialized_address_book

def parse_command(user_input: str):
    parsed_input = user_input.split()
    if len(parsed_input) >= 2 and parsed_input[0].lower() in COMMANDS_WITH_SPACE:
        parsed_input[0] = " ".join(parsed_input[:2])
        parsed_input.pop(1)
    return parsed_input

def handle_cmd_hello():
    return "\nHow can I help you?"

@input_error
def handle_cmd_add(ab_instance: AddressBook):
    name_to_add = input("ADD >> Name to add/update: ").strip().lower()
    phone_to_add = input("ADD >> Phone to add: ").strip()
    
    for name, record in ab_instance.data.items():
        if name_to_add == name.value.lower():
            record.add_phone(Phone(phone_to_add))
            added = f"ADD >> Phone {phone_to_add} added to {name_to_add.title()}."
            return added

    record = Record(Name(name_to_add))
    record.add_phone(Phone(phone_to_add))
    ab_instance.add_record(record)
    added = f"ADD >> {name_to_add.title()} added with phone {phone_to_add}."
    return added

@input_error
def handle_cmd_edit(ab_instance: AddressBook):
    name_to_edit = input("EDIT >> Name to edit: ").strip().lower()

    for name, record in ab_instance.data.items():
        if name_to_edit == name.value.lower():
            actual_name = name.value.lower()
            phones = [phone.number for phone in record.phones]
            print(f"EDIT >> Editing {actual_name.title()}; PHONES - {', '.join(phones)}")
            old_phone = input("EDIT >> Enter the phone number to edit: ")
            new_phone = input("EDIT >> Enter the new phone number, or type \"delete\" to remove: ")

            if new_phone == "" or new_phone == "delete":
                record.remove_phone(old_phone)
                edited = f"EDIT >> {actual_name.title()}'s phone number {old_phone} has been removed."
            else:
                record.edit_phone(old_phone, new_phone)
                edited = f"EDIT >> {actual_name.title()} has been updated."
    
    return edited

@input_error
def handle_cmd_delete(ab_instance: AddressBook):
    name_to_delete = input("DELETE >> Name to delete: ").strip().lower()
    for name, record in ab_instance.data.items():
        if name_to_delete == name.value.lower():
            actual_name = name.value
            confirmation = input("DELETE >> Confirm y/n: ")
            if confirmation.lower() == "y":
                ab_instance.remove_record(name)
                deleted = f"DELETE >> {actual_name.title()} was deleted."
                return deleted
            else:
                deleted = f"DELETE >> {actual_name.title()} remains on record."
    return deleted

@input_error
def handle_cmd_search(ab_instance: AddressBook):
    search_criteria = input("SEARCH >> Search name: ").strip().lower()
    search_result = ab_instance.search_records(search_criteria)
    contacts_list = []
    for record in search_result:
        phones = [phone.number for phone in record.phones]
        contacts_list.append(f"{record.name.value.title()}; Phones - {', '.join(phones)}")
    search = "SEARCH >> Result\n\n    " + "\n    ".join(contacts_list)
    return search

def handle_cmd_show_all(ab_instance: AddressBook):
    contacts_list = []
    for contact_name, record in ab_instance.data.items():
        phones = [phone.number for phone in record.phones]
        contacts_list.append(f"{contact_name.value.title()}; Phones - {', '.join(phones)}")
    show_all = "SHOW ALL >> Result\n\n    " + "\n    ".join(contacts_list)
    return show_all

def handle_cmd_exit():
    return "\n" + "Good bye!".center(50) + "\n"

def main():

    contacts_dictionary = {
    "beata wilk": ["506456245"],
    "joanna kura": ["602167448", "226207020"],
    "alicja czajkowska": ["228359164"],
    "piotr kowalski": ["502446239"],
    "andrzej zieliński": ["601887990", "700345788", "226106573"],
    }

    # ab_instance = initialize_address_book(contacts_dictionary)          # with emails
    ab_instance = initialize_address_book(contacts_dictionary)        # just phones

    print("\n" + return_bot_version().center(50))

    while True:

        user_input = input("\nEnter command:")

        if user_input:
            parsed_command, *arguments_list = parse_command(user_input)
        else:
            parsed_command = ""

        if parsed_command.lower() in EXISTING_COMMANDS:
            if parsed_command.lower() == "hello":
                print(handle_cmd_hello())
            elif parsed_command.lower() == "add":
                print(handle_cmd_add(ab_instance))
            elif parsed_command.lower() == "edit":
                print(handle_cmd_edit(ab_instance))
            elif parsed_command.lower() == "delete":
                print(handle_cmd_delete(ab_instance))
            elif parsed_command.lower() == "search":
                print(handle_cmd_search(ab_instance))
            elif parsed_command.lower() == "show all":
                print(handle_cmd_show_all(ab_instance))
            elif parsed_command.lower() in EXIT_COMMANDS:
                print(handle_cmd_exit())
                break
        else:
            print(f"Command \"{parsed_command}\" was not recognized.\nEXISTING COMMANDS >> {', '.join(EXISTING_COMMANDS)}")

if __name__ == "__main__":
    main()

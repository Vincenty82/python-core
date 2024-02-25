from datetime import datetime

class Field:
    def __init__(self, input_value = None):
        self.value = input_value

    @property # makes life so much easier
    def value(self):
        return self.internal_value
    
    @value.setter 
    def value(self, input_value):
        self.internal_value = input_value

class Name(Field):
    """
    Name
    geter - Not needed, but overide is here just in case it would be required to complete the task.
    setter - Overrides setter from Field. 
    """
    # @property
    # def value(self):
    #     return self.internal_value

    @Field.value.setter
    def value(self, input_value: str):
        if not input_value:
            raise ValueError("Name cannot be empty.")
        self.internal_value = input_value

class Phone(Field):
    """
    Phone
    geter - Not needed, but overide is here just in case it would be required to complete the task.
    setter - Overrides setter from Field. 
    """
    # @property
    # def value(self):
    #     return self.internal_value

    @Field.value.setter
    def value(self, input_value: str):
        if input_value and not input_value.strip().isdigit():
            raise ValueError("Must be a number.")
        self.internal_value = input_value

class Birthday(Field):
    """
    Birthday
    geter - Not needed, but it is here just in case it would be required to complete the task.
    setter - Overrides setter from Field. 
    """
    # @property
    # def value(self):
    #     return self.internal_value

    @Field.value.setter
    def value(self, input_value: str):
        if input_value and not datetime.strptime(input_value, "%Y-%m-%d"):
            raise ValueError("Wrong date format. Expected YYYY-MM-DD.")
        self.internal_value = input_value

class Record:
    """
    Record
    __init__ - Initiates name and optional phone and birthday fields.
    days_to_birthday - Compares today with birthday, if exists, and reutrns delta between now and upcoming birthdays. Otherwise returns None. 
    """
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)

    @property
    def days_to_birthday(self):
        if self.birthday.value:
            today = datetime.today()
            birthday_date = datetime.strptime(self.birthday.value, "%Y-%m-%d")
            upcoming_birthday_date = datetime(today.year, birthday_date.month, birthday_date.day)
            if today > upcoming_birthday_date:
                upcoming_birthday_date = datetime(today.year + 1, birthday_date.month, birthday_date.day)
            delta = upcoming_birthday_date - today
            return delta.days
        else:
            return None

class LogicalPuzzle:
    """
    __init__ - Sets records as a list.
    add_record - Appends records to the list.
    iterator - Returns records based on page number and number of records per page.
    """
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def iterator(self, page_num, page_size):
        index_start = (page_num - 1) * page_size
        index_end = min(index_start + page_size, len(self.records))
        return self.records[index_start:index_end]

def dirty_unpack(table):
    """
    Used to add test data
    """
    data_set = LogicalPuzzle()
    for row_key, data in table.items():
        record = Record(row_key, data[0], data[1])
        data_set.add_record(record)
    return data_set

def paginate_data(data_set, starting_page, records_per_page=5):
    """
    Used to paginate data output
    """
    records_page = data_set.iterator(starting_page, records_per_page) # Use puzzling iterator method. 
    if not records_page:
        print()
        print("The End".center(100))
        print()
        return
    print()
    print(f"Page {starting_page}".center(100))
    print()
    for record in records_page:
        output = record.name.value.title()
        if record.phone.value:
            output += "    Phone number: " + record.phone.value
        if record.birthday.value:
            output += "    Date of birth: " + record.birthday.value + "    Birthday in " + str(record.days_to_birthday) + " day(s)"
        print(output)
    next_page = starting_page + 1
    return next_page

def set_records_per_page():
    """
    
    """
    while True:
        try:
            choice = int(input("How many recors per page: "))
            break
        except Exception:
            print("Only numbers accepted!")
    return choice

def main():

    table = {
    "beata wilk": ("506456245", "1992-03-04"),
    "joanna kura": ("602167448", "1995-02-12"),
    "alicja czajkowska": ("228359164", "1982-12-03"),
    "piotr kowalski": ("502446239", "1970-07-12"),
    "andrzej zieliński": ("601887990", "1995-4-7"),
    "piotr fronczewski": (None, None),
    "fiodor dostojewski": (None, "2000-03-01"),
    "fryderyk szopen": ("123456789", None),
    "stanisław wokulski": ("234567890", "1976-04-13"),
    "izabela łęcka": ("345678901", "1986-08-19"),
    "beata kowalska": ("456789012", "1984-11-06"),
    "franek herbert": ("567890123", "2004-05-17"),
    "jaonna tuwim": ("678901234", "2005-06-06"),
    "andrzej kura": ("789012345", "1997-07-07"),
    "franek kimono": ("890123456", "1999-09-03"),
    }

    data_set = dirty_unpack(table)
    records_per_page = set_records_per_page()
    page = 1
    while True:
        next_page = paginate_data(data_set, page, records_per_page)
        if next_page:
            page = next_page
        else:
            break

if __name__ == "__main__":
    main()

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

import gspread
import re
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('contact_book')
CONTACTS = SHEET.worksheet('contacts')


def start():
    """
    Start menu that give users options to choose between 6 different tasks.
    """
    print("""
                --------MENU--------
                1. Add new contact\n\
                2. View all contacts\n\
                3. Delete a contact\n\
                4. Search contact\n\
                5. Reset contactbook\n\
                6. Exit\n
                    """)
    while True:
        choise = input("Choose the number of the option you want to choose: \n")
        if choise == '1':
            print("Add new contact...\n")
            add_new_contact()
            break
        elif choise == '2':
            print("Open Contact Book...\n")
            show_all_contacts()
            break
        elif choise == '3':
            print("Delete a contact...\n")
            print("You have to search for the contact you want to delete\n")
            search_contact()
            break
        elif choise == '4':
            print("Search menu...\n")
            search_contact()
            break
        elif choise == '5':
            print("Reset contact book...\n")
            validate_reset()
            break
        elif choise == '6':
            print("Exit programme...")
            exit_programme()
            break
        else:
            print("Not a valid input please enter a number 1-6")


def add_new_contact():
    """
    Add a new contact with first name, last name, phone number and email
    and check so the user input is correct, otherwise a error shows.
    """
    add_new_contact = {}

    while True:
        first_name = input("First Name: \n").capitalize()
        valid = first_name
        if not first_name.capitalize():
            print("Please enter First Name with letters a-z")
        else:
            break
    add_new_contact["FIRST NAME"] = first_name

    while True:
        last_name = input("Last Name: \n").capitalize()
        if not last_name.capitalize():
            print("Please enter Last Name with letters a-z")
        else:
            break
    add_new_contact["Lname"] = last_name

    while True:
        """
        To valid phone number using help from
        https://www.sololearn.com/Discuss/2588446/solved-python-phone-number-validator
        """
        phone_number = input("Phone Number: \n")
        pattern = r"^[0-9]"
        match = re.match(pattern, phone_number)
        if match and len(phone_number) <= 11:
            break
        else:
            print("Inavalid, Not more than 11 digits")
            continue
    add_new_contact["Number"] = phone_number

    while True:
        email = input("E-Mail: \n")
        if validate_email_input(email):
            break
        else:
            continue
    add_new_contact["E-Mail"] = email

    valid = check_double('First Name', first_name)

    if not valid:
        print("-----------------------------------")
        print("ADDED:\n")
        print(f"Name: {first_name.upper()} {last_name.upper()}")
        print(f'Number: {phone_number}')
        print(f'E-Mail: {email}\n')
        print("-----------------------------------")

        return update_worksheet_contact(add_new_contact)
    else:
        print("Contact with this name already exist")
        back_to_menu()


def check_double(column, name):
    """
    function that check if the name user input in add_new_contact already
    exist, so there is no doublicate contacts
    """
    print("loading...")
    check = CONTACTS.find(name)
    return check


def validate_email_input(email):
    """
    check if the input email is validate
    using help from this site:
    https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.fullmatch(regex, email)):
        return True
    else:
        print("E-Mail is invalid, please try again")
        return False   


def back_to_menu():
    """
    User get a question if
    they want to go back to menu or quit.
    """
    while True:
        user_choise = input("Back to menu: B, Quit programme: Q \n")
        if user_choise == "B" or user_choise == "b":
            start()
            break
        elif user_choise == "Q" or user_choise == "q":
            exit_programme()
            break
        else:
            print("Invalid input, Try again")
            back_to_menu()
            break
        return False


def add_one_more():
    """
    Giving the user the choise to add new contact 
    instead of get to start menu after adding a contact.
    """
    while True:
        again = input("Add another contact: A, Back to menu: B \n")
        if again == "A" or again == "a":
            add_new_contact()
            break
        elif again == "B" or again == "b":
            start()
            break
        else:
            print("Invalid input, Try again")
            add_one_more()
        return False


def update_worksheet_contact(add_new_contact):
    """
    Updating the google sheet with new contact informaion in contactbook.
    Provides a validation message that the update is complete.
    """
    new_worksheet = SHEET.worksheet('contacts')
    new_worksheet.append_row([x for x in add_new_contact.values()])
    print("Contact is now saved successfully! \n")
    add_one_more()


def show_all_contacts():
    """
    Function to show all the contacts from google sheet
    
    """
    get_all = CONTACTS.get_all_records()
    if get_all:
        for contact in get_all:
            printing_all_contacts(contact)
    else:
        print("Contactbook is empty!\n")
    back_to_menu()


def printing_all_contacts(existing):
    """
    Function that takes all the existing contacts from worksheet
    and make it a loop with the headers as title and the contact
    information as info in a list for each contact.
    """
    one_contact = []
    for title, info in existing.items():
        print(f'{title}: {info}')
    print("-----------------------------------")
    return one_contact


def search_contact():
    """
    Search function with a menu for the user to enter what
    they are searching for in contact book.
    """
    print("----SEARCH:----")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. E-Mail")
    print("5. Back to Menu\n")
    while True:
        search_input = input("Please enter a number 1-5: \n")
        if search_input == '1':
            get_from_search('First Name')
        elif search_input == '2':
            get_from_search('Last Name')
        elif search_input == '3':
            get_from_search('Phone Number')
        elif search_input == '4':
            get_from_search('E-Mail')
        elif search_input == '5':
            start()
        else:
            print("Not a valid number, try again")
            search_contact()
            break
        return False

def get_from_search(find_search):
    """
    Get input from user in search task, from name, number and email
    """
    if find_search == 'First Name':
        find_object = input('First Name: \n').capitalize()
        fname = find_column('First Name', find_object)
        search = fname
    elif find_search == 'Last Name':
        find_object = input('Last Name: \n').capitalize()
        lname = find_column('Last Name', find_object)
        search = lname
    elif find_search == 'Phone Number':
        find_object = input('Phone Number: \n')
        number = find_column('Phone Number', find_object)
        search = number
    elif find_search == 'E-Mail':
        find_object = input('E-Mail: \n')
        mail = find_column('E-Mail', find_object)
        search = mail
    else:
        print("Not a valid input, Try again")

    if search:
        for row_value in (search):
            row_number = row_value.row
            value_list = CONTACTS.row_values(row_number)
            listToStr = ' '.join([str(elem) for elem in value_list])

            print("------------------------------------------")
            print(listToStr)
            print("------------------------------------------")
            delete_one(row_number)
    else:
        print("Contact not found, Try search again\n")
        search_contact()


def find_column(column, value):
    """
    Get the cell row number and column number of the
    contact that the user is searching for
    """
    print("searching......\n")
    column_match = CONTACTS.findall(value)

    return column_match


def delete_one(contact):
    """
    A Function to remind the user before deleting contacts.
    
    """
    delete = input("Do you want to delete this contact? Y/N: \n")
    while True:
        if delete == 'Y' or delete == 'y':
            print("Deleting.....\n")
            delete_row(contact)
        elif delete == 'N' or delete == 'n':
            print("Not deleted!\n")
            back_to_menu()
            break
        else:
            print("Invalid input, Try again")
            break
        return False


def delete_row(row):
    """
    This function delete the row of the specific contact.

    """
    deleted_contact = CONTACTS.delete_rows(row)
    print("Contact is now succesfully deleted\n")
    start()
    return deleted_contact


def reset_contactbook():
    """
    Deleting the worksheet.
    All values clear, but the headers/titles appear on the first row again.

    """
    print("delete all contacts...\n")
    CONTACTS.clear()
    values = ("First name", "Last Name", "Phone Number", "E-Mail")
    new_sheet = CONTACTS.append_row(values)
    print("Phone Book is now reset!\n")
    back_to_menu()
    return new_sheet


def validate_reset():
    """
    Remind the user about thier actions in deleting the contacts

    """
    reset = input("Are you sure you want to reset? Y/N: \n")
    while True:
        if reset == 'Y' or reset == 'y':
            reset_contactbook()
            break
        elif reset == "N" or reset == "n":
            back_to_menu()
            break
        else:
            print("Not a valid input, Try again!")
            break
        return False
    


def main():
    """
    contains all the functions for the program
    """
    start()
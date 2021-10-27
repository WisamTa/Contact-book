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


def main():
    """
    contains all the functions for the program
    """
    start()
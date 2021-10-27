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


def main():
    """
    contains all the functions for the program
    """
    start()
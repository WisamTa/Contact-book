User Stories
As a user I want...

..that the program is simple to understand.
.. to get feedback when navigate thrue the app.
.. to add contact, be able to see all my saved contacts and to delete one or all.
.. ways to get back to menu easy.

Site Owner Goals
As a developer of this program, my goals was..

..To build a program that can store and add information.
..Make it easy for user to understand and how to use it.
..To make functions that add and store user inputs in API google sheets.
..Create functions like add a contact, open exisiting contacts and delete.
..Make a readable code as much as possible. 
..strengthen my comprehension about user experience design because it will be my next course to study if needed.
..Trying to think when using the app like an unsophisticated user. 

![This is an image](assest/images/flowchart.jpg)
The Structure is what you can see in the flowchart here. There is six different task from a menu that get the user to the different functions depending on what the user input. Every function has a way to get back to the menu or quit the programme after the task is done. In the flowchart every function has a own colour just to make it easy to follow.

Features

Existing Features

Start Menu
Programme starts with welcome message and a list of choises. The inputs the number of what task they want to follow and the program open that function.
![This is an image](assest/images/start.png)

Add a new contact
When add a new contact. User need to fill in first name, last name, phone number and email and then the information will be saved in the worksheet gspread.
Validation message when the user have correctly enter all the information.
Error message if user put more than 11 digits on phone number, and if user enter letters in phone numbers.
Error message is user have not entered a valid email address.
![This is an image](assest/images/Addnewcontact.PNG)

View all existing contacts
This function will open all the existing contacts that are saved in the worksheet and print them out.
Gives a choise to go back to menu or quit program.
![This is an image](assest/images/viewallcontact.PNG)

Delete one contact
Number 3 from the menu is to delete contact, the user has to search for the contact first by inputing one of the five options, first name, last name, email or phone number otherwise option number five is a kind of reminder to go back to menu or in other word an option to delete the delete option. 
![This is an image](assest/images/deletecontact.PNG)

Search contact
An option for search after a contact by typing one of the four categories of searching or a fifth option to go bach to menu.
Gives a error message if no contact could be find.
![This is an image](assest/images/search.PNG)

This feature will reset the worksheet.Only the headers-row in the worksheet will remain for store new contacts.
![This is an image](assest/images/search.PNG)

Exit program
This feature exit the programme and can be reach from some of the other features also.
Provide a message with a See you next time.
![This is an image](assest/images/Exit.PNG)

Features Left to Implement
From the worksheet on google i left information about addresses and didn't use in the project, i plan to mybe widen the information about contacts so it can include new categories like Addresses, Workoccupation, family members.... etc

Technologies Used
Language
Python3 - This project is written by Python as a the programming language.

Other programmes
Google sheets - To get  google sheet document (gspread) for store the information the user insert, and to remove information.
Gspread - The API to connect  to the programme.
GitHub - Hosting website.
Gitpod -  Workspaces.
Heroku - for deployment.
PEP8 - To validate python code
Re - to import re library for using regrexpressions for email validation.
and few other  famous websites for helping coders and explaining the concepts widely. 

Validator Testing
Valid code, passed on pep8 
![This is an image](assest/images/Pep8.PNG)

Bugs
No bugs left on the deplyed verstion.

Deployment
This project is deplyed on heroku with connection to github and using the code institue template. 

Deployed link 
https://contact-book123.herokuapp.com/
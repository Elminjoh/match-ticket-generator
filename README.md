# Football Match Tickets Genarator

This module defines classes for a Football Match Ticket Generator 
## Detailed Documantion of Modules

# User_ticket Class

The [User_Ticket] class represents all the user details and matches available for the user to pick from,

Attributes:
: - *full_name(str):*This is the users full name.
  - *email(str):*This is the users email.
  - *phone_number(str):*This is the users phone number.
  - *home_address(str):*This is the users home address.
  - *post_code(str):*This is the users post code.
  - *seat_number(str):*This is the users seat number.
  - *fixture(str):*This is the match the user picks from the series of matches available.
  - *ticket_ID(str):*This is a unique ID number that is generated and helps identify the user and the details on the ticket.

  Methods:

  : - 

        **\_\_init\_\_(full_name,email,phone_number,home_address,post_code,seat_number,fixture,ticket_ID):**

        : initializes a new user 
        :param full_name: The users full name
        :param email: The email address of the user
        :param phone_number: The Phone nu,ber of the user
        :param home_address: The users home address
        :param post_code: The users post code
        :param seat_number: The users seat number
        :param fixture: The fixture the user decides to pick
        :param ticket_ID: The users ticket ID number

        : intializing a a set of matches, stored a dictionary
        :param match : a set of matches for users to choose form 
  : -

        **create_ticket(self)**
        : This function collects all the required details needed for creating the ticket while setting parameters in place to make sure the information the user has entered is valid. There is a json function in use which stores the users details entered and makes it accessible to view usere details for future use and reference. I have used While loops as well which contains try and except functions in order to set the parameters needed for the user enetring their details and letting them know if the information enetered is correct or not.  
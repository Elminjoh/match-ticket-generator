#ticket generator project   ``
import json
import re
from pprint import pprint
import random


class User_Ticket:

    def __init__(self,full_name='felix', email='elmi@gmail.com', phone_number='07934343443', home_address='45 adrenaline road', post_code='e173gr', seat_number='f5', fixture= "Liverpool vs Manchester United", ticket_ID = "EL081907"):

        self.match =  {
            1:"Manchester United vs Liverpool", 
            2:"Nottingham Forest vs Derby United",  
            3:"Leicester City Women vs Liverpool Women", 
            4:"Real Madrid vs Barcelona", 
            5:"Arsenal Women vs Paris Saint-Germain Women"
        } 

        
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.home_address = home_address
        self.post_code = post_code
        self.seat_number = seat_number
        self.fixture = fixture
        self.ticket_ID = ticket_ID
        self.user_database = []
        
    def create_ticket(self):

        #loading the exisiting file for users
        try:
            with open('user_database.json', 'r') as json_file:
                self.user_database = json.load(json_file)
        except:
            self.user_database =[]
        
        while True :
            try :
                full_name = input("Enter your full name. ")
                if full_name == '':
                    print ("Inavild input") 
                    continue
                else: 
                    self.full_name = ' '.join([name.capitalize() for name in full_name.split(' ')])
                    break
                    
            except Exception as e:
                (f"invalid text entered....Error : {e}")
              
        while True :
            try :
                email = input ("Enter your email address. ")
                if email == '':
                    print("invalid Input")
                    continue
                else:
                    regex = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+"
                    if re.match(regex, email):
                        print ("Email address has been saved successfully")
                        self.email = email 
                        break
                    else:
                        print('invalid email..try again')
                        continue

            except Exception as e:
                (f"invalid text entered....Error : {e}")

        while True :
            try :
                phone_number =input ("Enter your Phone number.")
                if phone_number =='':
                    print("invalid Input")
                    continue

                elif len(phone_number) < 11 and len(phone_number) > 11:
                    print ("Invalid phone number")
                    continue
                else:
                    self.phone_number = phone_number
                    print('phone number has been sucessfuly saved')
                    break

            except Exception as e:
                (f"invalid text entered....Error : {e}")

        while True :
            try :
                home_address = input ("Enter Home address ")
                if home_address =='':
                    print("invalid Input")
                    continue

                else:
                    self.home_address = home_address
                    break

            except Exception as e:
                (f"invalid text entered....Error : {e}")

        while True :
            try :
                post_code = input ("Enter your post code. ")
                if post_code =='':
                    print("invalid Input")
                    continue

                else:
                
                    print ("post code has been saved successfully")
                    self.post_code = post_code
                    break

            except Exception as e:
                (f"invalid text entered....Error : {e}")

        while True :
            print('these are the matches available..\n')
            pprint(self.match)
            try :
                fixture = int(input ("What match would you like to watch ? "))
                print(fixture)
                if fixture == 1:
                    print ("you chose Manchester United vs Liverpool")
                    self.fixture = self.match [1]
                    break
                    
                elif fixture == 2:
                    print ("you have chose Nottingham Forest vs Derby United")
                    self.fixture = self.match [2]
                    break

                elif fixture == 3:
                    print ("you have chosen Leicester City Women vs Liverpool Women")
                    self.fixture = self.match [3]
                    break

                elif fixture == 4:
                    print ("you have chosen Real Madrid vs Barcelona")
                    self.fixture = self.match [4]
                    break

                elif fixture == 5:
                    print ("Arsenal Women vs Paris Saint-Germain Women")
                    self.fixture = self.match [5]
                    break
                else :
                    print ("invalid input")
                    continue
            
            except ValueError:
                print('you have entered an invalid number')


        my_range = 6
        my_random = random.randint(10**(my_range - 1 ) , 10**my_range -1 )
        self.ticket_ID = self.full_name[0:2].upper() + str(my_random)

        new_user = {
            'User Full Name' : self.full_name,
            "User Email" : self.email,
            "User Phone Number" : self.phone_number,
            "User Home Address" : self.home_address,
            "User Post Code" : self.post_code,
            "User Fixture" : self.fixture,
            "User Ticket ID" : self.ticket_ID
        }

        print('here is your ticket...\n')
        pprint(new_user)

        self.user_database.append(new_user) 

        with open('user_database.json', 'w') as json_file:
            json.dump(self.user_database, json_file)

user_1 = User_Ticket()
user_1.create_ticket()

    
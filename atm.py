import random
import time
import progressbar
import numpy as np
import json
import sqlite3
from sqlite3 import Error
import os



userDatabase ={5332077270: ['joseph', 'kithome', 'jmulingwakithome.jmk@gmail.com', 'password1',7800],1890789781: ['jacks', 'jaymoh', 'jacks.jmk@gmail.com', 'password2',5000]}
bankname ='JosephBank'

# def sql_database():
#     conn = sqlite3.connect('Client_data.db') #Opens Connection to SQLite database file.
#     conn.execute('''CREATE TABLE Client_db
#                 (FIRSTNAME            BLOB NOT NULL,
#                 LASTNAME         BLOB NOT NULL,
#                 PASSWORD         BLOB NOT NULL,
#                 EMAIL            BLOB  NOT NULL,
#                 ACCONTNUMBER     BLOB NOT NULL  
                
#                 );''') #Creates the table
#     conn.commit() # Commits the entries to the database
#     conn.close

def main():
    #setting the selected option to be false when user has not selected anything
    isValidOption = False

    print('Do you have an account with %s' %bankname)
    
    while isValidOption  == False:
        selectedOption = int(input('1:yes 2:No\n'))
        if (selectedOption==1):
            isValidOption = True
            login()

        elif(selectedOption==2):
            isValidOption = True
            
            register()
        else:
            print('Invalid option')
            
        
       

def login():
     #  # read the json file containing your database
    with open('UserDatabase.json','r') as mydb:
        json_data = json.load(mydb)
        print(json_data)

    print('***********Login**********')
    account_number =int(input('Enter your Account number:'))
    userpassword =input('Enter password:')

    #loop through the database which is dictionary datatype 
    for accountNumber,userAccountDetails in userDatabase.items():

        #if account number provided by user matches the one in database
        if(accountNumber == account_number):

            # if password matches the one in database
            if(userAccountDetails[3] == userpassword):
                bankOperations(userAccountDetails)
            print('Incorrect password')    
                   
        print('Account number doesn\'t  exist in our database')  
        login()          

def register():
    print('*********Register*********')
    firsname =input('Enter your firstname: :')
    lastname =input('Enter your lastname :')
    email = input('Enter your email address :')
    password =input('Enter password :')
    #   password2 =input('Confirm password :')

    accountNumber = generationAccountNumber()

    # create user for the generated random  account number
    userDatabase[accountNumber] =[firsname,lastname,email,password]

    time.sleep(0.1)
    print('Creating account,Please wait...')

    time.sleep(0.3)

    print('Generating account number')
    for i in progressbar.progressbar(range(100)):
        time.sleep(0.02)
        
    time.sleep(0.1)
    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")
    
    #saving the created user in a json file
    with open('UserDatabase.json', 'w') as file:
        json.dump(userDatabase, file)
    

    login()

        
def generationAccountNumber():

    return random.randrange(1111111111,9999999999)

def bankOperations(user):
    print('Welcome %s %s' %(user[0],user[1]))  

    isChoiceValid = False

    while isChoiceValid ==False:
        selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) transfer (4) Logout (6)exit \n")) 

        if(selectedOption ==1):
            isChoiceValid =True
            deposit(user)

        elif(selectedOption==2):
            withdraw(user)
            isChoiceValid =True
            
        elif(selectedOption ==3):
            isChoiceValid =True
            transfer(user)
            
        elif(selectedOption==4):
            isChoiceValid =True
            logout()  
        elif(selectedOption == 5):
            exit()    
        else:
            print("Invalid option selected")
            
                        
def deposit(user):
    # current_balance = 50000
    current_balance = get_balance(user) 
    deposit = int(input('How much do you want to deposit?\n'))
    final_balance = get_balance() + deposit
    print('Deposit successful\n Balance: %d' %final_balance ,'\n Thankyou and welcome again')
    bankOperations(user)

def transfer(user):
    current_balance = get_balance(user)
    transfer_amount = int(input('How much do you want to transfer?\n'))
    if transfer_amount < current_balance:
        if transfer_amount < 500:
            account_number2 = get_account(user)
            transfer_account =int(input("Please enter account number to transfer funds:"))
            balance = current_balance - amount
            print('Transfer success\n Account balance is  %d:' %balance ,'\n transfered to account number %d' %transfer_account)

            for account,value in userDatabase.items():
                if account == transfer_account:
                    amount = int(input('Please enter amount to transfer:'))
                    if account == account_number2:
                        balance = current_balance - amount
                        print('Transfer success\n Account balance is  %d:' %balance ,'\n transfered to account number %d' %account)

        


    
def withdraw(user):
    current_balance = 50000
    amount = int(input('How much do you want to withdraw?\n')) 
    balance = current_balance - amount
    print('Withdrawal successful')
    print('Getting your cash ready  %s'  %user[0])
    for i in progressbar.progressbar(range(20)):
        time.sleep(0.2)
    print("Take your cash : %d" %amount) 
    print('Current balance : %d' % balance)   
    bankOperations(user)

def get_balance(user):
    return user[4]

def get_account(user):
    return user[0] #This gets the account number    

def logout():
    login()        
      


main()           


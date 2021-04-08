import random
import time
import progressbar
import numpy as np
import json



userDatabase ={}
bankname ='JosephBank'

def main():
    print('Do you have an account with %s' %bankname)
    
    selectedOption = int(input('1:yes 2:No\n'))

    if (selectedOption==1):

        login()

    elif(selectedOption==2):
        
        register()
    elif(selectedOption >2):
        print('Option out of range,Would you like to Register?')
        revert()
       
       

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
        print(account_number)
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

    with open('UserDatabase.json', 'w') as file:
        json.dump(userDatabase, file)
    

    login()

        
def generationAccountNumber():

    return random.randrange(1111111111,9999999999)

def bankOperations(user):
    print('Welcome %s %s' %(user[0],user[1]))  

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n")) 

    if(selectedOption ==1):
        deposit(user)
    elif(selectedOption==2):
        withdraw(user)
    elif(selectedOption ==3):
        logout()
    elif(selectedOption==4):
        exit()  
    else:
        print("Invalid option selected")
        bankOperation(user)
                    
def deposit(user):
    current_balance = 50000
    deposit = int(input('How much do you want to deposit?\n'))
    final_balance = current_balance + deposit
    print('Deposit successful\n Balance: %d' %final_balance ,'\n Thankyou and welcome again')
    bankOperations(user)

def transfer(user):
    current_balance = 50000
    deposit = int(input('How much do you want to deposit?\n'))
    final_balance = current_balance + deposit
    print('Deposit successful\n Balance: %d' %final_balance)
    bankOperations(user)
    
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
def logout():
    login()        
      


main()           


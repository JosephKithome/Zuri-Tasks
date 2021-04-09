import random
database ={}

def init():
    isValidoption =False
    print('Welcome to BANK Joseph')

    while isValidoption ==False:
        haveaccount =int(input('Do you have an account with us 1.Yes 2. No :'))

        if (haveaccount ==1):
            isValidoption =True
            login()

        elif(haveaccount==2):
            isValidoption =True
            register()
        else:
            print('You have selected an Invalid option') 


def login():
    print('Welcome to bank Joseph')
    print('*********LOGIN********')

  
    account_number = int(input('Enter your account number:'))
    password = input('Enter your password:')

    
    isLoginSuccess = False
    while isLoginSuccess ==False:
        for accountNumber,userdetails in database.items():
            if (accountNumber == account_number):
                if (userdetails[2] == password):
                    isLoginSuccess = True
                    bankOps(userdetails)
                
                print('Invalid credentials') 
            print('Invalid options')           

def register():
    print('Register Here') 
    #collecting user inputs to register

    firstname =input('Enter firstname\n')
    lastname =input('Enter lastname\n')
    password =input('Enter password\n')
    email =input('Enter email address :')
    accountNumber = generateAccountNumber()

    database[accountNumber] =[firstname,lastname,email,password]
    print(accountNumber)
    login()



def generateAccountNumber():
    print('Genarating account number')
    return random.randrange(1111111111,9999999999)
    print(generateAccountNumber())

def bankOps(user):
    isOptionValid = False
    print('Welcome %s %s' % (user[0], user[1])) 
    print('Select an option\n 1.Withdraw \n 2.Deposit \n 3.Transfer \n 4.log out \n 5.Exit')

    while isOptionValid == True:
        selectedOption = int(input('Enter an option \n'))

        if(selectedOption ==1):
            isOptionValid ==True
            withdraw()
        elif (selectedOption ==2):
            isOptionValid ==True
            deposit()
        elif (selectedOption == 3):
            isOptionValid ==True
            transfer()
        elif (selectedOption ==4):
            isOptionValid ==True
            exit()
        elif(selectedOption ==5):
            isOptionValid ==True
            logout()   
        else:
            print('Invalid choice,Please try again')                  


def withdraw():
    print('How much do you want to withdraw?')    


def deposit():
    print('How much do you want to deposit?')   


def transfer():
    print('How much do you want to transfer?')  

def logout():
    login()          
        

init()


import datetime
def authentication():
    date = datetime.datetime.now()
    name = input("Please enter your username :")
    users =['joseph','jackson','jase']
    passwords = ["password1","password2","password3"]
    amountPresent = 10000

    if(name in users):
        password = input("Please insert password :")
        namePosition =users.index(name)
        print(namePosition)

        if (password == passwords[namePosition]):
            print("Welcome %s" %name + " logged in on " + str(date.strftime("%x")))
            print("Customer Service")
            print("1 . Withdraw")
            print("2. Deposit")
            print("3. Complaint")


            def Withdraw():
                amount=int(input("How much would you like to withdraw:"))
                
                print("take your cash %d" %amount) 
                current_balance =amountPresent -amount
                print('Current Balance %d :' %current_balance)   

            def Deposit():
                deposit=int(input("How much would you like to Deposit:"))
                current_balance =amountPresent + deposit
                print("current balance %d :" %current_balance)    

            def Complaint():
                complaint=input("What issue will you like to report:")
                print("Thank you for contacting us %s " %complaint)  

            selectedOption = int(input("Please select an option :"))
            if (selectedOption == 1):
                Withdraw()
                    
                
            elif(selectedOption ==2):
                Deposit()  
            
                
            elif (selectedOption==3):
                Complaint()
                
            else:
                print("Invalid option selected")
        
        else:
            print("incorrect password")
    else:
        print("Name not Found!")          

authentication()
      


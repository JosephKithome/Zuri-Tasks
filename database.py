import os

import account_Validation

user_dbpath ="data/user_record/"

def create(account_number,user_details):
    creationState = False 
    f=open(user_dbpath + str(account_number)+ ".txt","x")

    try:
        f.write(str(user_details))

    except FileExistsError:
        print("User already exists")
        delete(account_number)

    else:
        f.write(str(user_details))  
        creationState =True  


    finally:
        f.close()
        return creationState


def read(user_account_number):
    is_valid_ac_number = account_Validation.account_number_validation(user_account_number)
    try:
        if is_valid_ac_number:

            f=open(user_dbpath + str(user_account_number)+ ".txt","r")
        else:
            f=open(user_dbpath + user_account_number+ "r")


    except FileNotFoundError:
        print("User not found!!") 
        
    except FileExistsError:
        print("User doesn't exist") 
    except TypeError:
        print("Invalid account number format")     

    else:
        return f.readline()

def update(user_account_number):
    print("update record")

def delete(user_account_number):
    is_delete_success = False
    if os.path.exists(user_dbpath + str(user_account_number)+ ".txt"):
        try:
            os.remove(user_dbpath + str(user_account_number)+ ".txt")
            is_delete_success = True

        except FileNotFoundError:
 

            print("User not found!") 

        finally:
            return is_delete_success          

def does_email_exist(user_account_number,email):

    all_users = os.listdir(user_dbpath)
    
    for user in all_users:
        print(read(user))
        print("\n")

does_email_exist(1609386227,'juliameer@gmail.com')




def account_number_validation(account_number):
    # checking if account_number is empty
    if account_number:
        #checking whether it has 10 digits
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True

            except ValueError:
                print('Invalid account Number,Should only be integers') 
                return False
                
            except TypeError:
                print("Invalid account number")   
                return False    

        else:
            print('Account number cannot be  less or more than 10 digits')
            return False

def validate_register_inputs(input):
    pass
  
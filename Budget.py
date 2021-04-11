class Budget:

    def __init__(self,categories):
        self.categories = categories
        

    def Deposit(self,amount):
            deposit = int(input('Enter deposit amount:'))
            balance =amount + deposit
            return f'Depost successfull new balance is {balance}'
            

    def Withdrawal(self,amount):
        withdraw = int(input('Enter amount to withdraw:'))
        balance = amount -withdraw
        return f'Withdraw is successfull new balance is {balance}'


    def  Balance(self):
        print('Your balance is:')

    def transfer(self,amount):
        tranfer = int(input('Enter amount to transfer'))   
        newBalance =amount + tranfer
        return f'Your transfer is  successfull new  balance is {newBalance}'

food = Budget('Food')
clothing = Budget('clothing')
entertainment = Budget('Budget') 

print(food.Withdrawal(20))
print(clothing.transfer(40))
print(entertainment)


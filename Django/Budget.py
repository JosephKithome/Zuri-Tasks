class Budget:

    def __init__(self,categories, amount = 0):
        self.categories = categories
        self.amount = amount




    def Deposit(self,amount):
            deposit = int(input('Enter deposit amount:'))
            balance =amount + deposit
            return f'Depost of {self.amount} is successfull new balance is {balance}'
            

    def Withdrawal(self,amount):
        withdraw = int(input('Enter deposit withdraw:'))
        balance =amount + deposit
        return f'Withdraw of {self.amount} is successfull new balance is {balance}'


    def  Balance(self,amount):
        pass

    def transfer(self,amount):
        pass    

food = Budget('Food')
clothing = Budget('clothing')
entertainment = Budget('Budget')    

print(food.Deposit(20))
print(clothing)
print(entertainment)


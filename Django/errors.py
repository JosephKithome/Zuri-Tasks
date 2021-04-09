def calc(num1,num2):
    return num1/num2
try: 
    num1 = int(input('Enter number 1\n'))
    num2 = int(input('Enter number 2\n'))

    division = calc(num1,num2)
    print(division)

except TypeError:
    print('You cant divide a number by zero')
else:
    print('No Type error')    
finally:
    print('This would print out irrespective of an error')    


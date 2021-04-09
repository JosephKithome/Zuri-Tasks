class CustomException(Exception):
    pass

class ValueTooSmallException(CustomException):
    pass

class ValueTooBigException(CustomException):
    pass

number = 20
while True:

    try:
        input_number= int(input("Enter a  number :"))
        if input_number < number:
            raise ValueTooSmallException

        elif input_number > number:
            raise ValueTooBigException
              
        break    

    except ValueTooSmallException:
        print("Value too small") 
          

    except ValueTooBigException:

        print('Value too big')  

    except Exception as e:
        print(e.__str__())     

print('Hey you got it right,Keep it up')          

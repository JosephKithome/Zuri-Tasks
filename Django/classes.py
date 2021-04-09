class Cars:
    """
    This is a car class
    """
    def __init__(self,name,color,drive):
        self.name =name
        self.color = color
        self.drive =drive
        """
        This is a method of the car class
        """
    def accel(self):
        print(f'the {self.color} {self.name} which is a {self.drive} accelerates at 100mph')    

car_1 = Cars('Mercedes','red','4wheel')
car_2 = Cars('V8','white','6wheel')
car_1.accel()
car_2.accel()
print(help(Cars))

# print(car_1.name)
# print(car_2.name)


#     pass
# print(type(Cars))

# #instantiating a class
# car1 =Cars()
# print(type(car1))

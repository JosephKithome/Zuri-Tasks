class Animal:
    
    #class variables are 
    animal_type = 'Mammals'
    counter = 0

    def __init__(self,name,legs):
        #instance variables
        self.name = name
        self.legs = legs
        Animal.counter +=1

    #instance methods
    def can_run(self):
        print(f'Animal {self.name} runs with {self.legs}')    

    #used to change the state of a class method
    @classmethod
    def can_see(cls):
        print('Animal can see') 
    #static methods
    @staticmethod
    def tail_wiggle():
        print('Animal can wiggle its wings')    


animal_one =Animal('Rat',4)
animal_two = Animal('cat',6)
print(animal_one.animal_type)
print(animal_two.animal_type) 
print(Animal.counter)

print("##"*20)
animal_one.can_run()
animal_two.can_run()

print("##"*60)
animal_one.can_see()
animal_two.can_see()

animal_one.tail_wiggle()
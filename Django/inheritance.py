class Animal:
    def can_breathe(self):
        print('Can breathe')
   


    def Birds(Animal):
        pass

class Mammals(Animal):
    def body_size(self):
        return 'Mammals have a weight of over 40kgs'

mammal_one = Mammals().can_breathe()
mammal_two = Mammals()
print(mammal_one)
print(mammal_two.body_size())

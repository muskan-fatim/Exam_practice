#polymerphism 
class Animal:
    
    def sound (self , sound):
        print("Animal sound is ", sound)

class Dog(Animal):

    def sound(self , sound):
        print("Animal sound is ", sound)

class Cat(Animal):

    def sound(self , sound):
        print("Animal sound is ", sound)

animal = Animal()
dog = Dog()
cat = Cat()
print(animal.sound("singing"))
print(dog.sound("barking"))
print(cat.sound("meowing")) 
# polymerphism is the process of resuing parent method into child  or using a differnt function on differnt class with same name 
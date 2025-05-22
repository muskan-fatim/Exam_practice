# there are four pilar of OOP programing 
 # 1 inheritance
 # 2 polymerphasim
 # 3 Encapsulation 
 # 4 abstraction

#Inheritance 
class person():
    def __init__(self , name , number):
        self.name = name 
        self.number = number

parent = person("Muskan", 8905)

class child(person):
    def __init__(self, salary):
        super()__init__( name , number):
        self.salary = salary 
childern  = child("Muskan", 8905, 10,000)




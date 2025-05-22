# distractacture overriding overloading __str__ method 

# overriding is the method of override the content 
#  for exaple two function with same name but have differnt content
#  parent method or child method have same name method but it override 
# parents return string.

class person ():
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def Intro (self):
        return f"{self.name} is {self.age} year old "

class teacher(person):
    def __init__(self , name ,age):
       super().__init__(name , age)
    def Intro (self):
        return f"My name is {self.name} and I am teaching from many years and my age is now {self.age}"
# __str__ Method return string you don't need to call like a class method because it automatically return when you try to print simple class

class person2 ():
    def __init__(self , name , father):
        self.name = name
        self.father = father
    def __str__(self):
        return f"I am such a str method "
per1 = person("Muskna",20)
per2 = person2("ali", 30)
teach = teacher("tanzeel",20)
print(per1.Intro())
print(per2)

# distructor method
class person3 ():
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def __del__(self):
        print("Destructor is called")

per3 = person3("Muskna",20)
del per3
print(per3)
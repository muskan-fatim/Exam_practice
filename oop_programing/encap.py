class Encapsulation:
    def __init__(self, name, age):
        self._name = name  # protected variable
        self.__age = age    # private variable

    def get_name(self):
        return self._name

    def set_name(self, name): # setter method
        self._name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")
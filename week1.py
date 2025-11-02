"""
OOP concept demonstration in python
Week1 Assignment Code
"""

#Base Class
class Employee:
    """
    Basically, base class demonstrate encapsulation using private and protected attributes.
    """
    def __init__(self, name, age, salary):
        self._name = name      #protected
        self._age = age        # protected 
        self.__salary = salary #private attribute 

        def set_name(self, name): 
            self._name = name 

        def get_name(self): 
            return self._name 
        
        def set_age(self, age): 
            if age > 0: 
                self._age = age 
            else: 
            print("Age should not be negative or less than 0.") 

        def get_age(self):
            return self._age

    def set_salary(self, salary):
        if amount > 0:
           self.__salary = salary
        else:
            print("Salary should not be negative or less than 0.")

    def get_salary(self):
        return self.__salary

    def work(self):
        """ This method actually defined work of different employee like for dev defferent work description and same goes to manager."""
        return print(f"{self._name} is working.")
    def __str__(self):
        return f"General Employee(Name: {self.get_name()}, Age: {self._age}, Salary: {self.__salary})"

#Derived Class is Developer
# Basically, derived class demonstrate inheritance and polymorphism.
class Developer(Employee):
    """ This is child class or derived class that is derived from parent class Employee"""
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)  # Calling the constructor of the base class
        self.programming_language = programming_language

    # This method demonstrates polymorphism by overriding the work method of the base class.
    def work(self):
        return print(f"{self.get_name()} is coding in {self.programming_language}. At the age of {self._age}, he is earning good amount of money which is {self.get_salary()}.")

    # This is function is only available for child class which is unique to the parent class.
    def debug(self):
        print(f"{self.get_name()} is debugging code using {self.programming_language}.")

# Another Derived Class is Manager
class Manager(Employee):
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size
    def work(self):
        return print(f"{self.get_name()} is managing a team of {self.team_size} members.")

#....................................
# Testing the classes
# ......................................

#Creating objects of each class
emp1 = Employee("Himal Tamang", 30, 70000)
dev1 = Developer("Sujan Shrestha", 25, 80000, "Python")
mana1 = Manager("Anil Karki", 40, 90000, 10)

# Demonstrating encapsulation
print("Encapsulation:")
print(emp1)  # Using __str__ method to print employee details
emp1.set_name("Himal Tamang Updated")
print(f"Updated Name: {emp1.get_name()}")
print(emp1)
print("\n")
print("---Enheritance and Polymorphism---")
emp1.work()  
dev1.work() 
mana1.work()  
dev1.debug()  

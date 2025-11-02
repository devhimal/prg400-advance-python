class Employee:
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
        return print(f"{self._name} is working.")
    def __str__(self):
        return f"General Employee(Name: {self.get_name()}, Age: {self._age}, Salary: {self.__salary})"

class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)  # Calling the constructor of the base class
        self.programming_language = programming_language

    def work(self):
        return print(f"{self.get_name()} is coding in {self.programming_language}. At the age of {self._age}, he is earning good amount of money which is {self.get_salary()}.")

    def debug(self):
        print(f"{self.get_name()} is debugging code using {self.programming_language}.")

class Manager(Employee):
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size
    def work(self):
        return print(f"{self.get_name()} is managing a team of {self.team_size} members.")


emp1 = Employee("Himal Tamang", 30, 70000)
dev1 = Developer("Sujan Shrestha", 25, 80000, "Python")
mana1 = Manager("Anil Karki", 40, 90000, 10)

print("Encapsulation:")
print(emp1)  
emp1.set_name("Himal Tamang Updated")
print(f"Updated Name: {emp1.get_name()}")
print(emp1)
print("\n")
print("---Enheritance and Polymorphism---")
emp1.work()  
dev1.work() 
mana1.work()  
dev1.debug()  

'''Define a base class Employee with attributes name (string) and role (string), and a method display() that prints the employee’s name and role.
Create a class Trainer that inherits from Employee, adds an attribute specialization (string), and includes a display() method to print the trainer’s name, role, and specialization.
Create a class YogaInstructor that inherits from Employee, adds an attribute yoga_style (string), and includes a display() method to print the yoga instructor’s name, role, and yoga style.
Create a class MultiTrainer that inherits from both Trainer and YogaInstructor, includes both specialization and yoga_style attributes, and has a display() method to print the multi-trainer’s name, role, specialization, and yoga style.
Create one object from each class (Employee, Trainer, YogaInstructor, MultiTrainer) with sample data.
Display the details of each object by calling its display() method'''

class Employee:
    def __init__(self,name,role):
        self.name = name
        self.role = role
    def display(self):
        print(f"Employee's name: {self.name} , role:{self.role}")
class Trainer(Employee):
    def __init__(self, name, role,specialization):
        Employee.__init__(self,name, role)
        self.specialization = specialization 
    def display(self):
        print(f"Trainer name: {self.name} , role:{self.role} , specialization: {self.specialization}")
class YogaInstructor(Employee):
    def __init__(self, name, role,yoga_style):
        Employee.__init__(self,name, role)
        self.yoga_style = yoga_style
    def display(self):
        print(f"name: {self.name} , role:{self.role} , yoga style: {self.yoga_style}")

class MultiTrainer(Trainer,YogaInstructor):
    def __init__(self, name, role, specialization,yoga_style):
        Trainer.__init__(self,name, role, specialization) 
        YogaInstructor.__init__(self, name, role,yoga_style)
    def display(self):
        print(f"name: {self.name} , role:{self.role} , specialization: {self.specialization} , yoga style: {self.yoga_style} ")    

E1 = Employee("Arjun","Trainer")
T1 = Trainer("Arjun","Trainer","xxxx")  
Y1 = YogaInstructor("Rahul","yoga","yyyyyyy")  
M1 = MultiTrainer("Neeraj","Trainer","fitness","hhhhh")

E1.display()
T1.display()
Y1.display()
M1.display()
   

"""A company wants to create a simple system to define and display employee profiles based on their role types for record-keeping purposes. You are tasked with creating classes to represent different types of individuals in Python. Complete the following steps:

Create a class Person with attributes name (string) and age (integer), and a method show_details() that prints the person’s name and age.
Create a class Employee that inherits from Person, adds an attribute employee_id (string), and includes a show_details() method to print the employee’s name, age, and employee ID.
Create a class PartTime that inherits from Person, adds an attribute working_hours (float), and includes a show_details() method to print the part-time worker’s name, age, and working hours.
Create a class Consultant that inherits from both Employee and PartTime, adds an attribute project_name (string), and includes a show_details() method to print the consultant’s name, age, employee ID, working hours, and project name.
Create one object of each class (Person, Employee, PartTime, Consultant) with sample data.
Display the details of each object by calling its show_details() method"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id):
        Person.__init__(self, name, age)  
        self.employee_id = employee_id

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")


class PartTime(Person):
    def __init__(self, name, age, working_hours):
        Person.__init__(self, name, age)   
        self.working_hours = working_hours

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Working Hours: {self.working_hours}")


class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Employee.__init__(self, name, age, employee_id)
        PartTime.__init__(self, name, age, working_hours)
        self.project_name = project_name

    def show_details(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Working Hours: {self.working_hours}, Project: {self.project_name}"
        )


p1 = Person("Reshma", 27)
e1 = Employee("Hari", 26, "20344")
pt1 = PartTime("Anju", 22, 5.5)
c1 = Consultant("Binu", 30, "55678", 4.0, "AI System Upgrade")

p1.show_details()
e1.show_details()
pt1.show_details()
c1.show_details()

       
        

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
x = Calculator(a, b)
if operator == '+':
    print("Sum:", x.add())
elif operator == '-':
    print("Difference:", x.sub())
elif operator == '*':
    print("Multiplication:", x.mul())
elif operator == '/':
    if b != 0:
        print("Division:", x.div())
    else:
        print("Enter a non zero number")
else:
    print("Invalid operator")
    

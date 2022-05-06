class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        print(result)

    def minus(self):
        result = self.num1 - self.num2
        print(result)

    def multiply(self):
        result = self.num1 * self.num2
        print(result)

    def divide(self):
        result = self.num1 / self.num2
        print(result)

call = Calculator (1, 2)
call.add()    
call.minus()
call.multiply() 
call.divide()

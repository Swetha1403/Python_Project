class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

calc1 = Calculator(5, 3)
calc2 = Calculator(10, 2)

result1 = Calculator.add(calc1.value1, calc1.value2)
result2 = Calculator.subtract(calc2.value1, calc2.value2)

print("Result1:", result1)
print("Result2:", result2)

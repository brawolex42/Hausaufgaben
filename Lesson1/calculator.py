class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        if b == 0:
            raise ArithmeticError("На ноль делить нельзя")
        return a / b
    def pow(self, a, b=2):
        return a ** b
    def avg(self, nums):
        if len(nums) == 0:
            return 0
        return sum(nums) / len(nums)

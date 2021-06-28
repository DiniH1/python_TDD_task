class AdvancedCalc:

    def remain(self, num1, num2):
        return num1 % num2

    def percent(self, num1, num2):
        return (num1 / num2) * 100

    def positive(self, num1):
        if num1 > 0:
            return True
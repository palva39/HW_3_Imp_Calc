class Calculator:
    history = []
    @staticmethod
    def add(a: int, b: int) -> int:
        result = a + b
        Calculator.history.append((a, b, '+', result))
        return result

    @staticmethod
    def subtract(a: int, b: int) -> int:
        result = a - b
        Calculator.history.append((a, b, '-', result))
        return result

    @staticmethod
    def multiply(a: int, b: int) -> int:
        result = a * b
        Calculator.history.append((a, b, '*', result))
        return result

    @staticmethod
    def divide(a: int, b: int) -> int:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        Calculator.history.append((a, b, '/', result))
        return result
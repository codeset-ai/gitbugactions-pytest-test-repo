class Calculator:

    @staticmethod
    def sumInt(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def sumFloat(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def pi():
        with open("app/resources/pi.txt", "r") as f:
            pi = float(f.readline())
        return pi
    
    @staticmethod
    def golden():
        with open("app/resources/golden.txt", "r") as f:
            golden = float(f.readline())
        return golden
    
    @staticmethod
    def goldenpi():
        return Calculator.pi() * Calculator.golden()

    @staticmethod
    def square(a: int) -> int:
        return a * a
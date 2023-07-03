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
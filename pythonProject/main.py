# task1
squares = [x ** 2 for x in range(1, 11)]


# task2
def generate_squares(start, end):
    return [x ** 2 for x in range(start, end)]


# task3
class SquareGenerator:
    def generate_squares(self, start, end):
        return [x ** 2 for x in range(start, end)]


# task4
import math

square_generator = SquareGenerator()
squares = square_generator.generate_squares(1, 10)
square_roots = [math.sqrt(x) for x in squares]
print(squares)
print(square_roots)


# task5
def generate_squares5(self, start, end):
    if end < start:
        raise ValueError("End of range must be greater than start.")
    return [x ** 2 for x in range(start, end)]

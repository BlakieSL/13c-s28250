import math


class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("error")
        return [x ** 2 for x in range(start, end)]

    def square_roots(self, squares):
        return [math.sqrt(x) for x in squares]

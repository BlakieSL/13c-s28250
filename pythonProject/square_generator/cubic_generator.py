from .square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        return [x ** 3 for x in range(start, end)]

    def generate_squares(self, start, end):
        if start >= end:
            raise ValueError("Start of range must be less than the end.")
        return [x ** 2 for x in range(start, end)]
from .square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):

        if start >= end:
            raise ValueError("error")
        return [x ** 2 for x in range(start, end)]

    def generate_cubes(self, start, end):
        if start >= end:
            raise ValueError("error")
        return [x ** 3 for x in range(start, end)]

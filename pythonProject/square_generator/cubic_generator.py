from .square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        return [x ** 3 for x in range(start, end)]

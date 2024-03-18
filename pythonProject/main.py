squares = [x**2 for x in range(1, 11)]
def generate_squares(start, end):
    return [x**2 for x in range(start, end)]


squares = generate_squares(1, 11)
print(squares)
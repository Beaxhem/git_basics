import os
import sys
import math


class QuadraticEquationSolver:

    def equation_str(self, a, b, c):
        return f"({a}) x^2 + ({b}) x + ({c}) = 0"

    def _discriminant(self, a, b, c):
        return b * b - 4 * a * c

    def _get_roots(self, a, b, discriminant):
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)

    def solve(self, a, b, c):
        if a == 0:
            print("Error. a cannot be zero")
        print("Equation is:", self.equation_str(a, b, c))

        discriminant = self._discriminant(a, b, c)
        (x1, x2) = self._get_roots(a, b, discriminant)

        number_of_roots = 0
        if discriminant == 0 or x1 == x2:
            number_of_roots = 1
        elif discriminant > 0:
            number_of_roots = 2

        if not number_of_roots:
            print("There are no roots")
            return
        else:
            print(f"There are {number_of_roots} roots")
        
        print(f"x1 = {x1}")    
        if x1 != x2:
            print(f"x2 = {x2}")


def input_from_file(filename: str):
    if not os.path.isfile(filename):
        print(f"file {filename} does not exist")
        exit(1)

    with open(filename) as f:
        line = f.readline()
        input = line.split()

        if len(input) == 3:
            try:
                return [float(x) for x in input]
            except ValueError:
                print(f"Error. Expected a valid real number")  
            return input

        print("invalid file format")
        exit(1)

def get_value(name: str):
    while True:
        print(f"{name} = ", end="")
        value = input()
        try:
            return float(value)
        except ValueError:
            print(f"Error. Expected a valid real number, got {value} instead")

def input_from_command_line():
    a = get_value("a")
    b = get_value("b")    
    c = get_value("c")

    return (a, b, c)

def main(args):
    input = []
    if len(args) == 1:
        filename = args[0]
        input = input_from_file(filename)
    else:
        input = input_from_command_line()

    solver = QuadraticEquationSolver()
    solver.solve(*input)

if __name__ == "__main__":
    main(sys.argv[1:])    
import sys


def input_from_file(filename: str):
    pass

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

    # solver = QuadraticEquationSolver()
    # solver.solve(*input)

if __name__ == "__main__":
    main(sys.argv[1:])    
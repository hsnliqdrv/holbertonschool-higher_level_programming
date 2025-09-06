#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if (argv[2] == '+'):
        from calculator_1 import add as op
    elif (argv[2] == '-'):
        from calculator_1 import sub as op
    elif (argv[2] == '*'):
        from calculator_1 import mul as op
    elif (argv[2] == '/'):
        from calculator_1 import div as op
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, op(a, b)))

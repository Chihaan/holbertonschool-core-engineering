#!/usr/bin/env python3


from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{:d}".format(add(a, b)))
    print("{:d}".format(sub(a, b)))
    print("{:d}".format(mul(a, b)))
    print("{:d}".format(div(a, b)))

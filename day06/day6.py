import base64
from ctypes import *

file = open('input', 'r')
numbers = list(map(int, file.read().split(',')))

# initialise connection with c
# https://docs.python.org/3/library/ctypes.html
# https://stackoverflow.com/questions/56883980/pass-and-return-an-array-of-doubles-through-c-function-inside-python
# sorry for the in code declaration, i wanted to use the numbers python array, but i could not parse it over to c because the buffer size was to smal.
# IntPointer = POINTER(c_int)
# by = bytes(numbers)
# b = IntPointer.from_buffer_copy(by)
# test1(b, len(numbers), 256)
dll = CDLL("faster.so")
faster = dll.faster
array = (c_int * 300)(3, 3, 2, 1, 4, 1, 1, 2, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 4, 1, 1, 5, 2, 1, 1, 2, 1, 1, 1, 3, 5,
                      1, 5, 5, 1, 1, 1, 1, 3, 1, 1, 3, 2, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 4, 1, 3, 3, 1, 1, 3,
                      1, 3, 1, 2, 1, 3, 1, 1, 4, 1, 2, 4, 4, 5, 1, 1, 1, 1, 1, 1, 4, 1, 5, 1, 1, 5, 1, 1, 3, 3, 1, 3, 2,
                      5, 2, 4, 1, 4, 1, 2, 4, 5, 1, 1, 5, 1, 1, 1, 4, 1, 1, 5, 2, 1, 1, 5, 1, 1, 1, 5, 1, 1, 1, 1, 1, 3,
                      1, 5, 3, 2, 1, 1, 2, 2, 1, 2, 1, 1, 5, 1, 1, 4, 5, 1, 4, 3, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 5, 2, 1,
                      1, 1, 5, 1, 1, 1, 4, 4, 2, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 4, 4, 1, 4, 1, 1, 5, 3, 1, 1, 1, 5, 2, 2,
                      4, 2, 1, 1, 3, 1, 5, 5, 1, 1, 1, 4, 1, 5, 1, 1, 1, 4, 3, 3, 3, 1, 3, 1, 5, 1, 4, 2, 1, 1, 5, 1, 1,
                      1, 5, 5, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 2, 3, 1, 2, 2, 3, 1, 3, 1, 1, 4, 1, 1, 2, 1, 1, 1, 1, 3, 5,
                      1, 1, 2, 1, 1, 1, 4, 1, 1, 1, 1, 1, 2, 4, 1, 1, 5, 3, 1, 1, 1, 2, 2, 2, 1, 5, 1, 3, 5, 3, 1, 1, 4,
                      1, 1, 4)


def one_in_python():
    global numbers
    for i in range(18):
        nextGen = []
        for num in numbers:
            if num == 0:
                nextGen.extend([6, 8])
            else:
                nextGen.append(num - 1)
        numbers = nextGen
    print(len(numbers))


def one_in_c():
    fish = faster(array, 5, 80)


def two():
    fish = faster(array, 300, 256)
    print(fish)


def example_data():
    array_example = (c_int * 5)(3, 4, 3, 1, 2)
    d = faster(array_example, 5, 257)


# one_in_c()
two()
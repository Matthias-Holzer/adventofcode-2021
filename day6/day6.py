from ctypes import *

file = open('test','r')
numbers = list(map(int, file.read().split(',')))

def one():
    global numbers
    for i in range(18):
        nextGen = []
        for num in numbers:
            if num == 0:
                nextGen.extend([6,8])
            else:
                nextGen.append(num-1)
        numbers = nextGen
    print(len(numbers))


def two():
    #https://docs.python.org/3/library/ctypes.html
    #https://stackoverflow.com/questions/56883980/pass-and-return-an-array-of-doubles-through-c-function-inside-python

    dll = CDLL("faster.so")
    test1 = dll.faster
    test1.argtypes = POINTER(c_int),c_int,c_int
    test1.restype = c_int

    a = (c_int * 5)( 3,4,3,1,2 )
    d = test1(a,5, 18)
    #print(d)


    exit()

    c_code = "faster.so"
    c_func = CDLL(c_code)
    c_func.faster(numbers, len(numbers), 18)




#one()
two()
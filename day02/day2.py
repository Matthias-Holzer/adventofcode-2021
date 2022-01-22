file = open('input', 'r')
read = file.read().replace('\n',' ').split(" ")
numbers = [int(i) for i in read[1::2]]
data = read
data[1::2]=numbers
print(data)

def one():
    horizontal = 0
    vertical = 0
    for idx,d in enumerate(data[::2]):
        if d == 'forward':
            horizontal += data[idx*2+1]
        if d == 'up':
            vertical -= data[idx*2+1]
        if d == 'down':
            vertical += data[idx*2+1]

    print(horizontal)
    print(vertical)
    print(horizontal*vertical)

def two():
    horizontal = 0
    depth = 0
    aim = 0
    for idx,d in enumerate(data[::2]):
        if d == 'forward':
            horizontal += data[idx*2+1]
            depth += aim * data[idx*2+1]
        if d == 'up':
            aim -= data[idx*2+1]
        if d == 'down':
            aim += data[idx*2+1]
    print(depth*horizontal)


    print()

two()
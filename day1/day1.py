file = open('input', 'r')
read = file.read().splitlines()
numbers = [int(i) for i in read]

def one():
    counter = 0
    for idx,number in enumerate(numbers):
        if idx != 0:
            if number > numbers[idx-1]:
                counter += 1
    print(counter)

def two():
    counter = 0
    for idx, number in enumerate(numbers):
        if idx != 0:
            try:
                if number + numbers[idx - 1] + numbers[idx-2] > numbers[idx - 1] + numbers[idx-2] + numbers[idx-3]:
                    counter += 1
            except:
                if numbers > numbers[idx-1]:
                    counter += 1

    print(counter)

one()
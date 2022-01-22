file = open('message.txt', 'r')
read = file.read().splitlines()

def one():
    gamma = ''
    epsilon = ''
    for idx in range(12):
        cal = 0
        for line in read:
            cal += int(line[idx])
        if cal > (len(read)/2):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return  int(gamma, 2) * int(epsilon, 2)

def two_oxygen_generator_rating():
    data = read
    kill = ''
    for idx in range(12):
        if(len(data)==1):
            break
        cal = 0
        for line in data:
            cal += int(line[idx])
        if cal >= (len(data)/2):
            kill = '0'
        else:
            kill = '1'
        data2 = []
        for line in data:
            if line[idx] != kill:
                data2.append(line)
        data = data2
        print(data)
    print(int(data[0], 2))
    return int(data[0], 2)

def two_co2_scrubber_rating():
    data = read
    kill = ''
    for idx in range(12):
        if (len(data) == 1):
            break
        cal = 0
        for line in data:
            cal += int(line[idx])
        if cal >= (len(data) / 2):
            kill = '1'
        else:
            kill = '0'
        data2 = []
        for line in data:
            if line[idx] != kill:
                data2.append(line)
        data = data2
        print(data)
    print(int(data[0], 2))
    return int(data[0], 2)

#print(one())
print(two_oxygen_generator_rating() * two_co2_scrubber_rating())
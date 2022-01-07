file = open('input', 'r')
crabs = list(map(int, file.read().split(',')))

def part1():
    costs = []
    alternating = 0
    for crab in crabs:
        try_position = int(sum(crabs)/len(crabs))+alternating
        if alternating > 0:
            alternating += 1
        else:
            alternating += -1
        print(f"alternating {alternating} new mean {try_position}")
        alternating = int(alternating*-1)
        cost = 0
        for crab in crabs:
            x = int(try_position - crab)
            if x > 0:
                cost += x
            else:
                cost += x*-1
        costs.append(cost)
        print(min(costs))
    print(costs)

def part2():
    costs = []
    alternating = 0
    for crab in crabs:
        try_position = int(sum(crabs)/len(crabs))+alternating
        if alternating > 0:
            alternating += 1
        else:
            alternating += -1
        #print(f"alternating {alternating} new mean {try_position}")
        alternating = int(alternating*-1)
        cost = 0
        for crab in crabs:
            x = int(try_position - crab)
            if x > 0:
                cost += x*(x+1)/2
            else:
                cost += x*-1*(x*-1+1)/2
        costs.append(cost)
        print(min(costs))
    print(costs)
    print(min(costs))


#part1()
part2()
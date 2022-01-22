# solution form https://www.reddit.com/user/Codezilla996/
# as i want to improve my programming skills and learn new ways to solve problems i learn from people, that are better than me

from collections import Counter

file = open('input', 'r')
read = file.read().splitlines()

def one():
    points_with_vents = []
    for line in read:
        poit_start, point_end = line.split(' -> ')
        x_start, y_start = tuple(map(int, poit_start.split(',')))
        x_end, y_end = tuple(map(int, point_end.split(',')))
        #check horizontal and vertical
        if x_start == x_end or y_start == y_end:
            for x in range(min(x_start,x_end), max(x_start,x_end)+1):
                for y in range(min(y_start,y_end),max(y_start,y_end)+1):
                    points_with_vents.append((x,y))

    l = len([point for point in Counter(points_with_vents).values() if point>1])
    print(l)

def two():
    points_with_vents = []
    for line in read:
        poit_start, point_end = line.split(' -> ')
        x_start, y_start = tuple(map(int, poit_start.split(',')))
        x_end, y_end = tuple(map(int, point_end.split(',')))
        # check horizontal and vertical
        if x_start == x_end or y_start == y_end:
            for x in range(min(x_start, x_end), max(x_start, x_end) + 1):
                for y in range(min(y_start, y_end), max(y_start, y_end) + 1):
                    points_with_vents.append((x, y))
        #check for 54°
        else:
            xinc = 1 if x_start < x_end else -1
            yinc = 1 if y_start < y_end else -1
            y = y_start
            for x in range(x_start,x_end+xinc,xinc):
                points_with_vents.append((x,y))
                y += yinc

    l = len([point for point in Counter(points_with_vents).values() if point > 1])
    print(l)

one()
two()
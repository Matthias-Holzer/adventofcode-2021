with open('input', 'r') as fin:
    raw_data = fin.read().strip().split("\n")
    heat_map = [[int(i) for i in list(line)] for line in raw_data]

rows = len(heat_map)
columns = len(heat_map[0])

out = 0
low_points = []
for row in range(rows):
    for column in range(columns):
        # check top
        if not row == 0:
            if not heat_map[row][column] < heat_map[row - 1][column]:
                continue
        # check bottom
        if not row == rows - 1:
            if not heat_map[row][column] < heat_map[row + 1][column]:
                continue
        # check left
        if not column == 0:
            if not heat_map[row][column] < heat_map[row][column - 1]:
                continue
        # check right
        if not column == columns - 1:
            if not heat_map[row][column] < heat_map[row][column + 1]:
                continue
        out += heat_map[row][column] + 1
        low_points.append((row, column))

print(f"part1: {out}")
print(f"low_points: {low_points}")
## low_point[0] y axis (down)
## low_point[1] x axis (right)

end = False
points_in_basin = []
def points_around():
    global end
    old = points_in_basin
    for point in points_in_basin:
        # check up
        if not point[0] == 0 and heat_map[point[0]-1][point[1]] < 9:
            if not (point[0]-1, point[1]) in points_in_basin:
                points_in_basin.append((point[0]-1, point[1]))
        # check down
        if not point[0] == rows-1 and heat_map[point[0] + 1][point[1]] < 9:
            if not (point[0] + 1, point[1]) in points_in_basin:
                points_in_basin.append((point[0] + 1, point[1]))
        # check left
        if not point[1] == 0 and heat_map[point[0]][point[1] - 1] < 9:
            if not (point[0], point[1] - 1) in points_in_basin:
                points_in_basin.append((point[0], point[1] - 1))
        # check right
        if not point[1] == columns - 1 and heat_map[point[0]][point[1] + 1] < 9:
            if not (point[0], point[1] + 1) in points_in_basin:
                points_in_basin.append((point[0], point[1] + 1))
    if old == points_in_basin:
        end = True


sizes = []
for low_point in low_points:
    print(f"low_point: {low_point}")
    end = False
    points_in_basin = [low_point]
    while not end:
        points_around()
    print(f"points_in_basin: {points_in_basin}")
    sizes.append(len(points_in_basin))

print(f"sizes {sizes}")
sizes.sort()
print(f"part2: {sizes[-1]*sizes[-2]*sizes[-3]}")
file = open("input", "r")
lines = file.read().splitlines()
print(lines)

o = ['(', '[', '{', '<']
c = [')', ']', '}', '>']

p = {'(': ')', '[': ']', '{': '}', '<': '>'}

ill = []
toc = []
for line in lines:
    legal = True
    opb = []
    for b in line:
        if len(opb) == 0:
            opb.append(b)
            continue
        if b in o:
            opb.append(b)
            continue
        if b == p[opb[-1]]:
            opb.pop()
            continue
        ill.append(b)
        legal = False
        break
    if legal:
        toc.append(opb)

re = ill.count(')') * 3
re += ill.count(']') * 57
re += ill.count('}') * 1197
re += ill.count('>') * 25137
print(f"part one: {re}")


for line in toc:
    for idx, b in enumerate(line):
        line[idx] = c[o.index(b)]
    line.reverse()

rs = []
for line in toc:
    r2 = 0
    for c in line:
        r2 = r2 * 5
        if c == ')':
            r2 += 1
        elif c == ']':
            r2 += 2
        elif c == '}':
            r2 += 3
        elif c == '>':
            r2 += 4
    rs.append(r2)


rs.sort()
print(f"part two: {rs[int(len(rs)/2)]}")

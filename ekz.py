n = int(input())
groups = {}

for i in range(n):
    info = str(input()).split(" ")[2:]
    if int(info[1]) >= 8:
        if groups.get(info[0]) is None:
            groups[info[0]] = 1
        else:
            groups[info[0]] += 1

maximum = 0
for i in groups.items():
    if i[1] > maximum:
        maximum = i[1]

answer = []
for i in groups.items():
    if i[1] == maximum:
        answer.append(i[0])

answer.sort()
print(" ".join(answer))

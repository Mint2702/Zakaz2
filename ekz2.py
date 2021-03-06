n = int(input())
groups = {}


def get_groups(n):
    for i in range(n):
        mark = str(input()).split(" ")[2:]
        if int(mark[1]) >= 8:
            if groups.get(mark[0]) is not None:
                groups[mark[0]] += 1
            else:
                groups[mark[0]] = 1


get_groups(n)

max_mark = 0


def find_max():
    global max_mark
    for i in groups.items():
        if i[1] > max_mark:
            max_mark = i[1]


find_max()

result = []


def find_result():
    for i in groups.items():
        if i[1] == max_mark:
            result.append(i[0])


find_result()

result.sort()
print(" ".join(result))

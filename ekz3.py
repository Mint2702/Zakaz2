def input_results(n, results, count=0):
    while count < n:
        result = str(input()).split(" ")[2:]
        mark = int(result[1])
        if mark >= 8:
            if results.get(result[0]) is not None:
                results[result[0]] += 1
            else:
                results[result[0]] = 1

        count += 1


def find_max(results, max_mark=0):
    for i in results.items():
        if i[1] > max_mark:
            max_mark = i[1]

    return max_mark


n = int(input())
results = {}
input_results(n, results)
max_mark = find_max(results)

result = [i[0] for i in results.items() if i[1] == max_mark]
result.sort()

print(" ".join(result))

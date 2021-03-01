def input_forces() -> list:
    global n, k
    inp = str(input())
    inp = inp.split(" ")
    n = int(inp[0])
    k = int(inp[1])
    inp = str(input())
    inp = inp.split(" ")
    forces = [int(i) for i in inp]
    wins = {int(i): 0 for i in inp}
    return wins, forces


def check_if_won(wins: dict, diff: list, count: int) -> bool:
    values = list(wins.values())
    maximum1 = max(values)
    values.remove(maximum1)
    maximum2 = max(values)
    if count >= 100:
        diff.append(maximum1 - maximum2)
    for key, win in wins.items():
        if win == k or check_diff(diff):
            print(key)
            return True
    return False


def check_diff(diff: list):
    if len(diff) > 50:
        prev = diff[0]
        for i in diff:
            if i < prev:
                return False
            prev = i
        return True
    else:
        return False


wins, forces = input_forces()
player1 = forces[0]
diff = [0]
count = 0
while not check_if_won(wins, diff, count):
    count += 1
    player2 = forces[1]
    if player2 > player1:
        wins[player2] += 1
        player1 = int(player2)
        looser = forces.pop(0)
        forces.append(looser)
    else:
        wins[player1] += 1
        looser = forces.pop(1)
        forces.append(looser)

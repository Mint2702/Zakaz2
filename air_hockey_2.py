string1 = str(input()).split(" ")
n = int(string1[0])
k = int(string1[1])
string2 = str(input()).split(" ")

strength = [int(i) for i in string2]
num_of_wins = {int(i): 0 for i in string2}

player_won = strength[0]
counter = 0


def check_for_win(num_of_wins, counter, strength):
    if counter >= n * 2:
        print(max(strength))
        return True
    for key, win in num_of_wins.items():
        if win == k:
            print(key)
            return True
    return False


while not check_for_win(num_of_wins, counter, strength):
    counter += 1
    player_lost = strength[1]
    if player_lost > player_won:
        num_of_wins[player_lost] += 1
        player_won = int(player_lost)
        looser = strength.pop(0)
        strength.append(looser)
    else:
        num_of_wins[player_won] += 1
        looser = strength.pop(1)
        strength.append(looser)

inp = str(input())
inp = inp.split(" ")
prev = inp[0]
now = inp[1]
digts_prev = len(prev)
if (
    int(now[:digts_prev]) % int(prev) == 0
    or int(now[: digts_prev + 1]) % int(prev) == 0
):
    print("YES")
else:
    print("NO")

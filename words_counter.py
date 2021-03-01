from collections import Counter
import re

one = str(input()).lower()
two = str(input()).lower()

one = re.findall(r"[\w']+", one)
two = re.findall(r"[\w']+", two)

one = Counter(one)
two = Counter(two)

if one == two:
    print("YES")
else:
    print("NO")

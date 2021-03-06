from collections import Counter
import re


def input_string():
    string = str(input()).lower()

    return string


def convert(string):
    string = re.findall(r"[\w']+", string)

    return string


def output(counter1, counter2):
    if counter1 != counter2:
        print("NO")
    else:
        print("YES")


string1 = input_string()
string2 = input_string()

converted1 = convert(string1)
converted2 = convert(string2)

counter1 = Counter(converted1)
counter2 = Counter(converted2)

output(counter1, counter2)

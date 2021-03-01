string = str(input())


def check_end(string: str, counter: int, letter: str) -> int:
    if letter == "l":
        oe = "o"
    else:
        oe = "e"

    while counter < len(string) - 1 and string[counter] == oe:
        counter += 1
        if string[counter] == letter:
            return counter
    return False


for let in range(len(string) - 1):
    if string[let] == "l" and string[let + 1] == "o":
        counter = int(let) + 1
        counter_end = check_end(string, counter, "l")
        if counter_end:
            counter_end = len(string) - counter_end - 1
            print(counter_end)
            string = string[:let] + string[-counter_end:]
    if let >= len(string) - 2:
        break

print(string)

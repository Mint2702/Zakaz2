def input_row():
    row_str = str(input()).split(" ")
    row_int = [int(i) for i in row_str]
    return row_int


def compress(row):
    length = len(row)
    status = False
    compresed = []
    in_order = 0

    for index in range(length):
        if index == length - 1:
            if status and in_order > 1:
                new_element = "-%s," % row[index]
                compresed.append(new_element)
            elif status and in_order == 1:
                new_element = ",%s," % row[index]
                compresed.append()
            else:
                new_element = "%s," % row[index]
                compresed.append(new_element)
            break

        if row[index + 1] - row[index] == 1:
            in_order += 1
            if not status or in_order == 1:
                compresed.append(str(row[index]))
            status = True
            continue
        else:
            if status and in_order > 1:
                new_element = "-%s," % row[index]
                compresed.append(new_element)
            elif status and in_order == 1:
                new_element = ",%s," % row[index]
                compresed.append(new_element)
            else:
                new_element = "%s," % row[index]
                compresed.append(new_element)

        in_order = 0
        status = False

    return compresed


def print_result(row):
    result = "".join(row)[:-1]
    print(result)


row = input_row()
result = compress(row)
print_result(result)

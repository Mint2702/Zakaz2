inp = str(input()).split(" ")
row = [int(i) for i in inp]

new_row = []
status = False
count = 0
for i in range(len(row)):
    if i == len(row) - 1:
        if status and count > 1:
            new_row.append(f"-{row[i]},")
        elif status and count == 1:
            new_row.append(f",{row[i]},")
        else:
            new_row.append(f"{row[i]},")
        break

    if row[i + 1] - row[i] == 1:
        count += 1
        if not status or count == 1:
            new_row.append(f"{row[i]}")
        status = True
        continue
    else:
        if status and count > 1:
            new_row.append(f"-{row[i]},")
        elif status and count == 1:
            new_row.append(f",{row[i]},")
        else:
            new_row.append(f"{row[i]},")
        status = False
        count = 0

new_row_str = "".join(new_row)[:-1]
print(new_row_str)

def get_students():
    massive = str(input()).split(" ")
    students_on_start = massive[0]
    students_on_finish = massive[1]
    return students_on_start, students_on_finish


def check_for_devision(first, second):
    if int(second[: len(first)]) % int(first) == 0:
        return True
    elif int(second[: len(first) + 1]) % int(first) == 0:
        return True
    else:
        return False


students_on_start, students_on_finish = get_students()
if check_for_devision(students_on_start, students_on_finish):
    print("YES")
else:
    print("NO")

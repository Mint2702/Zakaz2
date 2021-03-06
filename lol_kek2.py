inp_string = str(input())
string_kek = "kek"
string_lol = "lol"
empty = ""


for i in range(10):
    inp_string = inp_string.replace(string_lol, empty)
    inp_string = inp_string.replace(string_kek, empty)
    string_kek = string_kek[:-1] + "ek"
    string_lol = string_lol[:-1] + "ol"

print(inp_string)

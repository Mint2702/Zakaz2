def input_filter(n):
    originals = {}
    for i in range(n):
        song_raw = str(input()).split("|")
        song = remove_spaces(song_raw)

        name = song[0]
        group = song[1]
        year = int(song[2])
        length = len(song)
        if length == 3 and year <= 2021:
            if originals.get(name) is None:
                originals[name] = [group, year]
            elif year >= originals[name][1]:
                continue
            else:
                originals[name] = [group, year]

    return originals


def remove_spaces(song):
    song = [j.strip() for j in song]

    return song


def dict_to_str(dict):
    origs_list = [f"{song[1][0]} - {song[0]}" for song in dict.items()]
    origs_list.sort()
    origs_str = "\n".join(origs_list)

    return origs_str


n = int(input())
originals = input_filter(n)

result = dict_to_str(originals)
print(result)

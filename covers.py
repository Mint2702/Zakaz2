n = int(input())
songs = {}
for i in range(n):
    song = str(input()).split("|")
    song = [j.strip() for j in song]
    name = song[0]
    song[2] = int(song[2])
    if len(song) == 3 and song[2] <= 2021:
        if songs.get(name) is None:
            songs[name] = [song[1], song[2]]
        elif song[2] >= songs[name][1]:
            continue
        else:
            songs[name] = [song[1], song[2]]


origs = [f"{song[1][0]} - {song[0]}" for song in songs.items()]
origs.sort()
print("\n".join(origs))

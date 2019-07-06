def stripString(str1):
        a = "!@#$%^&*()><:;,[]|\?/~`'."
        for b in a:
            str1 = str1.replace(b, '')

        return (str1.lower()).rstrip("\n")

def printLyr(filepath):
    file = open(filepath, "r")
    lyrics = []

    for cnt, line in enumerate(file):
        song = ""
        while file.readline() != "@@@@@@@@@@\n":
            song += " " + stripString(file.readline())
        lyrics.append(song)
        file.readline()

    file.close()
    return lyrics

def printLyr_d(filepath):
    file = open(filepath, "r")
    lyrics = []

    for cnt, line in enumerate(file):
        song = ""
        while file.readline() != "@@@@@@@@@@\n":
            song += " " + stripString(file.readline())
        lyrics.append(song)
        file.readline()

    file.close()
    return lyrics


filepath_eminem = "C:\\Users\Sakshum\Documents\GitHub\Lyric Project\Lyric-Classifier\eminem-lyrics"
eminem_list = printLyr(filepath_eminem)

filepath_drake = "C:\\Users\Sakshum\Documents\GitHub\Lyric Project\Lyric-Classifier\drake-lyrics2"
drake_list = printLyr_d(filepath_drake)

file = open("songsFormatted", "w+")
file_rappers = open("rappers", "w+")
for song in eminem_list:
    file.write(song + "\n")
    file_rappers.write(str(0) + "\n")

for song in drake_list:
    file.write(song + "\n")
    file_rappers.write(str(1) + "\n")

file.close()
file_rappers.close()








def stripString(str1):
        a = "!@#$%^&*()><:;[]|\?/~`'."
        for b in a:
            str1 = str1.replace(b, '')

        return (str1.lower()).rstrip("\n")

def printLyr(filepath):
    file = open(filepath, "r")
    lyrics = []

    while file.readline():
        song = ""
        while file.readline() != "@@@@@@@@@@\n":
            song += " " + stripString(file.readline())
        lyrics.append(song)

    file.close()
    return lyrics


filepath_eminem = "C:\Sakshum\MY STUFF\Random\Code Bits\eminem-lyrics-short.txt"
filepath_drake = "C:\Sakshum\MY STUFF\Random\Code Bits\drake-lyrics.txt"

eminem_list = printLyr(filepath_eminem)
drake_list = printLyr(filepath_drake)

file = open("songsFormatted", "w+")
for song in eminem_list:
    file.write(song + "\n"*2)






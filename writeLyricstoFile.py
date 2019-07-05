from scraper import scraper as scrap

em_lyr = open("eminem-lyrics1", "w")
drake_lyr = open("drake-lyrics1", "w")

eminem_songs = scrap.getSongs('eminem')
drake_songs = scrap.getSongs('drake') 

for song in eminem_songs:
    em_lyr.write(scrap.getLyrics(song, 'eminem'))
    em_lyr.write("@"*10 + "\n")

for song in drake_songs:
    drake_lyr.write(scrap.getLyrics(song, 'drake'))
    drake_lyr.write("@"*10 + "\n")

em_lyr.close()
drake_lyr.close()



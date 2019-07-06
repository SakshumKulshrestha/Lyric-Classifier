from scraper import scraper as scrap
import time

em_lyr = open("eminem-lyrics", "w")
drake_lyr = open("drake-lyrics2", "w")

eminem_songs = scrap.getSongs('eminem')
drake_songs = scrap.getSongs('drake') 

for song in eminem_songs:
    em_lyr.write(scrap.getLyrics(song, 'eminem'))
    time.sleep(2)
    em_lyr.write("@"*10 + "\n")

for song in drake_songs:
    drake_lyr.write(scrap.getLyrics(song, 'drake'))
    time.sleep(3)
    drake_lyr.write("@"*10 + "\n")

em_lyr.close()
drake_lyr.close()



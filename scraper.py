from bs4 import BeautifulSoup
import requests

class scraper: 

    def stripString(str1):
        a = "!@#$%^&*()><:;[]|\?/~`'. "
        for b in a:
            str1 = str1.replace(b, '')

        return str1.lower()

    def getLyrics(song, name):
        song = scraper.stripString(song)
        name = scraper.stripString(name)
        url = "https://www.azlyrics.com/lyrics/{}/{}.html".format(name.lower(), song.lower())
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        divset = soup.find_all("div", limit=22)
        lyrics = divset[len(divset)-1].text
        return lyrics

    def getSongs(name):
        name = str(name)
        url = "https://www.azlyrics.com/{}/{}.html".format(name[0], name)
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        songsList = []

        for title in soup.find_all(target="_blank"):
            songsList.append(scraper.stripString(str(title.text)))

        return songsList



scrap = scraper
artistName = 'eminem'
songs = scrap.getSongs(artistName)
print(songs[0])
print(scrap.getLyrics(songs[0], artistName))





        


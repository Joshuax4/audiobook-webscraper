#TODO - Skip files with .ogg in it.
#TODO - Currently downloads everything on the webpage, don't want that.
#TODO - Perhaps set CWD to downloads if able to.

import requests, bs4, os #os used to save to harddrive.
os.makedirs('Audiobooks', exist_ok=True) #makes folder. exist_ok = True stops an error occuring if folder already exists
url = input("Please copy 'archive.org' URL for the desired audio: ") #turn this into a command line url maybe
#TODO - Take input of archive.org link
#TODO - Directory takes input for name of folder, easier to sort audiobooks.
res = requests.get(url) #downloads the current new URL
res.raise_for_status()  #Checks the URL can be reached, throws exception and crashes program if error occurs
soup = bs4.BeautifulSoup(res.text, 'html.parser') #creates BeautifulSoup object
#soup.select finds all possible matches, so this is my list.
audioElem = soup.select('.stealth.download-pill') # .stealth.download-pill CONSISTENT IN AUDIOBOOKS ON ARCHIVE.ORG
print(audioElem)
linkNum = 0
for i in audioElem:
    audioURL = 'https://archive.org' + audioElem[linkNum].get('href')
    if '.mp3' in audioURL:
        print("Preparing download...")
        #TODO - If/else here for skipping downloads. If file = mp3, download, else - skip message ("File is not .mp3"
        # )
        print("Downloading Link: ", audioURL)
        res = requests.get(audioURL)
        res.raise_for_status()
        audioFile = open(os.path.join('Audiobooks', os.path.basename(audioURL.replace('%20', ' '))), 'wb')
        #TODO - Here is where I adjust the filename. Set it to variable, then pass str(variable) as .join args
        for chunk in res.iter_content(100000):
            audioFile.write(chunk)
        audioFile.close()
        linkNum += 1
        print("Next link...")
    else:
        print("Audio file not '.mp3', skipping..")
        print("Next link...")
        linkNum += 1
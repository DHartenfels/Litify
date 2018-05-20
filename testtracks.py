import requests
import csv
import json
xd= """
(     (                           
 )\ )  )\ )  *   )     (           
(()/( (()/(` )  /( (   )\ )  (     
 /(_)) /(_))( )(_)))\ (()/(  )\ )  
(_))  (_)) (_(_())((_) /(_))(()/(  
| |   |_ _||_   _| (_)(_) _| )(_)) 
| |__  | |   | |   | | |  _|| || | 
|____||___|  |_|   |_| |_|   \_, | 
                             |__/  
"""
print(xd)
r = requests.get("https://api.spotify.com/v1/me/top/tracks", headers={"Authorization": "Bearer BQD7AvA-cDNqCut4aH4Vj8vxJGwhcAfrzdcGjA84QTPve2sxI7ACXyGMPMCnmYuM8MzKJrm2VoXGG7Ka9emHOOIiIZ85ibqDyLhjKIAj3WUuJdy894mzCxSyBCrBU2jqeqv1lHU37vxdZKXa_s35AyoyTuLJLr9V6E5rFAfHcSts"})
w = r.status_code
p=0
list_artists = []
list_songs= []
list_spotifyurl = []
if w == 200:                                                                        #Only proceeds if the Response is 200
    x = r.json()["items"]                                                           #Searches the Response for the Key "Items"

    with open("tracks7.csv","w") as csvfile:                                        #Writes the collected Data into a CSV for processing later on
        f = csv.writer(csvfile)
        f.writerow(["Name of your top played Tracks","Spotify Track ID"])
        for elem in x:
            y = r.json()['items'][p]['artists'][0]['name']
            f.writerow([elem["name"], elem["id"]])                                  #selects the Keys specified here from the Dictonary and writes the Value into a row
            list_songs.append([elem['name']])
            list_artists.append(y)
            list_spotifyurl.append([elem['id']])
            p = p + 1


    with open("tracks7.csv","r") as file:                                           #opens the CSV file and prints the Data into the console
        fi = csv.reader(file, delimiter=',', quotechar='"')
        for i in fi:
            (', '.join(i))
    with open(r'tracks7.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(list_artists)
    for i in range(len(list_songs)):
        print(list_songs[i], list_artists[i])
    
else:
    print('Ungültiger API Status Code: ' + str(w))                                  #if the Response code is anything but 200 it'll get printed here for easy trubleshooting

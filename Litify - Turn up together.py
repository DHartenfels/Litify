import requests
import csv
import json

xd =  """
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
api_keys = []
list_artists = []
list_songs = []
list_spotifyurl = []
list_json_data = []
user_loop_anzahl = 0

def read_api(api_key):
    r = requests.get("https://api.spotify.com/v1/me/top/tracks", headers={"Authorization": "Bearer" + str(api_key)})
    list_json_data.append(r.json()["items"])

def get_top_tracks(json_data):
    p = 0
    for elem in json_data:
            y = r.json()['items'][p]['artists'][0]['name']
            f.writerow([elem["name"], elem["id"]])                                  
            list_songs.append([elem['name']])
            list_artists.append(y)
            list_spotifyurl.append([elem['id']])
            p = p + 1





erste_eingabe = input("Bitte geben Sie den ersten Auth Bearer ein: ")
api_keys.append(erste_eingabe)
abfrage_mehr_keys = input("Wollen Sie noch mehr Bearer eingaeben ? (y/anykey)")
while abfrage_mehr_keys == "y":
    #x = input("Bitte geben Sie den nächsten Bearer ein: ")
    api_keys.append(input("Nächster Bitte"))
    abfrage_mehr_keys = input("Wollen Sie noch einen Bearer eingeben?")
else:     
    while user_loop_anzahl <= len(api_keys):
        read_api(api_keys[user_loop_anzahl])
        get_top_tracks(list_json_data[user_loop_anzahl])
        user_loop_anzahl = user_loop_anzahl + 1

    for i in range(len(list_songs)):
        print(list_songs[i], list_artists[i])    

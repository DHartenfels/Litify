import requests
import json

api_keys = []
list_songs = []
list_artists = []
list_spotifyurl = []
user_loop = 0


def get_top_tracks(api_key):
    r = requests.get("https://api.spotify.com/v1/me/top/tracks", headers={"Authorization": "Bearer " + str(api_key)})
    jsondata = r.json()["items"]
    p = 0
    for elem in jsondata:
        y = r.json()['items'][p]['artists'][0]['name']
        list_songs.append([elem['name']])
        list_artists.append(y)
        list_spotifyurl.append([elem['id']])
        p = p + 1


erste_eingabe = input("Bitte geben Sie den ersten Auth Bearer ein: ")
api_keys.append(erste_eingabe)
more_keys = input("Wollen Sie noch mehr Keys eingeben? (y/anykey)")
while more_keys == "y":
    api_keys.append(input("Geben Sie den nächsten Auth Bearer ein: "))
    more_keys = input("Wollen Sie noch einen Key eingeben? (y/anykey)")

while (user_loop <= len(api_keys)):
    get_top_tracks(api_keys[user_loop - 1])
    if user_loop <= len(api_keys):
        user_loop += 1

for i in range(len(list_songs)):
    print(list_songs[i], list_artists[i])

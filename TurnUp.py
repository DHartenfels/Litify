import requests


api_keys = []
list_songs = []
list_artists = []
list_spotifyurl = []
user_loop = 0
list_songs_unique = []
list_artists_unique = []



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

xd= ("\n"
     "\n"
     "  _       _  _    _   __                   _                                        ___               _    _                 \n"
     " | |     (_)| |  (_) / _|                 | |                                      |__ \             | |  | |                \n"
     " | |      _ | |_  _ | |_  _   _   ______  | |_  _   _  _ __  _ __    _   _  _ __      ) | __ _   ___ | |_ | |__    ___  _ __ \n"
     " | |     | || __|| ||  _|| | | | |______| | __|| | | || '__|| '_ \  | | | || '_ \    / / / _` | / _ \| __|| '_ \  / _ \| '__|\n"
     " | |_ ___ | || |_ | || |  | |_| |          | |_ | |_| || |   | | | | | |_| || |_) |  / /_| (_| ||  __/| |_ | | | ||  __/| |  \n"
     " |______||_| \__||_||_|   \__, |           \__| \__,_||_|   |_| |_|  \__,_|| .__/  |____|\__, | \___| \__||_| |_| \___||_|   \n"
     "                           __/ |                                           | |            __/ |                              \n"
     "                          |___/                                            |_|           |___/                               \n"
     "\n")
print(xd)

first_input = input("Please enter the first Key: ")
api_keys.append(first_input)
more_keys = input("Do you want to add more Keys? (y/anykey)")
while more_keys == "y":
    api_keys.append(input("Please enter the next Key: "))
    more_keys = input("Do you want to add more Keys? (y/anykey)")

while (user_loop <= len(api_keys)):
    get_top_tracks(api_keys[user_loop - 1])
    if user_loop <= len(api_keys):
        user_loop += 1


print('These are your most listened Songs: ')
list_songs = list_songs[20:]
list_artists = list_artists[20:]
list_spotifyurl = list_spotifyurl[20:]

for i in range(len(list_songs)):
    print(str(i +1)+":", list_songs[i], list_artists[i])



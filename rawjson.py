import requests

r = requests.get("https://api.spotify.com/v1/me/top/tracks", headers={"Authorization": "Bearer BQAwFeMp2Kv-Y_fSGOczFTkQDwxEMzJ8GCjFCDGEH9QODOz-0exFWrFuDLuNgKRdUDh5Ya4NjZ__XF7d_O1BW2HKX5sVbhxdR03NOQ5u0FGg3FgLvYsp-FB1aL3KWRghK1XgfBKx8a2j-sbehodON4dDg8HKtDCKxw"})
print(r.status_code)
x = r.json()['items']

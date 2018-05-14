import requests
r = requests.get("https://api.spotify.com/v1/me/top/tracks",auth =('e99b63f0ab2e4d449844d3b2ec6e29ce','3156f94ebdd74dcba3b3e1025868921a'))
print(r.status_code)
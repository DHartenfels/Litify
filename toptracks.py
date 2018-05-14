import requests
import csv
import json
r = requests.get("https://api.spotify.com/v1/me/top/tracks", headers={"Authorization": "Bearer BQAeMKRM6MVSB-jRJ_W2U6j0SVzZBDosKZYmuKtpKINxlf8kTct-pvbV_e2TeHzaEDmADYzqt8-Sy-LZfBv85ZuccjZ-b9IBusNgKnd8EUpsbwqD_n_n5vHtlsJYgoCR6x62-S1hAKHGi6gPLnmQu-ggQ0rCjCdq7g"})
w = r.status_code
if w == 200:                #Only proceeds if the Response is 200
    x = r.json()["items"]   #Searches the Response for the Key "Items"
    with open("tracks5.csv","w") as csvfile: #Writes the collected Data into a CSV for processing later on
        f = csv.writer(csvfile)
        f.writerow(["Name of your top played Tracks","Spotify Track ID"])
        for elem in x:
            f.writerow([elem["name"], elem["id"]]) #selects the Keys specified here from the Dictonary and writes the Value into a row

    with open("tracks5.csv","r") as file: # opens the CSV file and prints the Data into the console
        fi = csv.reader(file, delimiter=',', quotechar='"')
        for i in fi:
            print(', '.join(i))
else:
    print('Ungültiger API Status Code: ' + str(w)) #if the Response code is anything but 200 it'll get printed here for easy trubleshooting

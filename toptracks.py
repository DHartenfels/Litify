import requests
import csv
import json
r = requests.get("https://api.spotify.com/v1/me/top/tracks", headers={"Authorization": "Bearer BQD_8QhdHdO6Ie7vfnEjF3iEe5ak7LcOoyS__Zw2Qd1Sm7P8ipmn8FmOgifHsj9QsB0ERZ_vVJWhVxALuE2ECpGgcugJa813NIZtN8nB1wk9XLStbw9uMrXGqTsntb6ZAPm5mYSUDRmt7tkW2E9TpH3s07X7joZmh19xY5QtVU2O"})
w = r.status_code
p=0
list = []
if w == 200:                #Only proceeds if the Response is 200
    x = r.json()["items"]   #Searches the Response for the Key "Items"

    with open("tracks7.csv","w") as csvfile: #Writes the collected Data into a CSV for processing later on
        f = csv.writer(csvfile)
        f.writerow(["Name of your top played Tracks","Spotify Track ID","Artist"])
        for elem in x:
             y = r.json()['items'][p]['artists'][0]['name']
             # print(y)
             f.writerow([elem["name"], elem["id"]]) #selects the Keys specified here from the Dictonary and writes the Value into a row
             list.append(y)
             p = p + 1
    # with open("track6.csv", "a",) as fp:
    #     wr = csv.writer(fp)
    #     wr.writerow(list)

        # if p <= 10:
        #     for elem in y:
        #         f.writerow
        #         p=p + 1
        #         print(p)

    with open("tracks7.csv","r") as file: # opens the CSV file and prints the Data into the console
        fi = csv.reader(file, delimiter=',', quotechar='"')
        for i in fi:
            (', '.join(i))
    with open(r'tracks7.csv', 'a') as f:
        writer = csv.writer(f)
        for val in list:
            writer.writerow([val])
else:
    print('Ungültiger API Status Code: ' + str(w)) #if the Response code is anything but 200 it'll get printed here for easy trubleshooting

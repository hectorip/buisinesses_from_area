import googlemaps
import json
import requests
import time
from t import types
api_key = ''
client = googlemaps.Client(key=api_key)
lat= 19.351291
long= -99.101664

lat = 19.350411
long = -99.093321
r = 590

lat = 19.355149
long = -99.087444
r = 170

def read_page(lat, long, t, next_page=None, page=0, r=475):
    print("Reading page page {} of type {}".format(page, t))

    if next_page:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        # r = requests.get(url,{"key": api_key, "pagetoken": next_page})
        time.sleep(5)
        r = requests.get(url,params={"key": api_key, "pagetoken": next_page})
        places = r.json()
        # print(places)
        # print(r.text)
        if places.get('status') == "INVALID_REQUEST":
            print("error")
            return
    else:
        places = client.places(
            query="",
            type=t,
            location="{},{}".format(lat, long),
            radius=r
        )
    with open("data/raw/{}_{}.json".format(t, page), mode="w") as f:
        f.write(json.dumps(places.get('results')))
    if places.get('next_page_token'):
        read_page(lat, long, t, places.get('next_page_token'), page+1, r)

for t in types:
    read_page(lat, long, t)
import csv
import json
import os

d = "data/raw"
rd = "result"

# load all to clean

places = {}
for f in os.listdir(d):
    print("Reading {}".format(f))
    with open("{}/{}".format(d, f), "r", encoding='utf8') as rf:
        text = rf.read()
        results = json.loads(text)
        for result in results:
            id = result.get("place_id")
            if places.get(id):
                print("repeated {}".format(id))
            else:
                places[id] = result

print("Total places: {}".format(len(places)))

k = os.getenv("GOOGLE_API_KEY")
with open("result/places.csv", "w", encoding='utf8') as rf:
    writer = csv.writer(rf)
    writer.writerow([
        "Nombre", "Dirección",
        "Tipos de negocio", "Link en maps", "latitud", "longitud", "Foto", "ID Google Places"])
    for i, p in places.items():
        ref = p.get("photos", [{}])[0].get("photo_reference")
        lat =  p.get("geometry").get("location").get("lat")
        long =  p.get("geometry").get("location").get("lng")
        row = [
            p.get("name"),
            p.get("formatted_address") or p.get("vicinity"),
            ",".join(p.get("types")),
            "https://www.google.com/maps/search/?api=1&query={},{}".format(lat, long),
            lat,
            long,
            "https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={}key={}".format(ref, k) if ref else "",
            p.get("place_id"),
        ]
        writer.writerow(row)

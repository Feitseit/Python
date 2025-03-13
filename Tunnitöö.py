import requests
import json


#json-andmete url
URL = "https://metshein.com/kordamine/json/tooted.json"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    tooted = data["tooted"]

#arvuta koguväärtus (hind * laoseis)
koguvaartus = sum(
    t["hind"] * t["laoseis"]
    for t in tooted
    if isinstance(t.get("hind"), (int,float)) and isinstance(t.get("laoseis"), int)
)

print(f"Koikide toodete koguvaartus laoseisu järgi: {koguvaartus:.2f} €")

#loenda tooted kategoorias "Toidukaubad"
toidukaubad_arv = sum(1 for t in tooted if t.get("kategooria") == "Toidukaubad")
print(f"toidukaupade arv: {toidukaubad_arv}")

#leia erinevad kategooriad
kategooriad = {t.get("kategooria") for t in tooted if "kategooria" in t}
print(f"erinevaid tootekategooriaid: {len(kategooriad)}")

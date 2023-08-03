import json
data = '''{
    "manchecter city" : "bruno fernandes",
    "real madrid" : "modritch",
    "PSG" : "neymar",
}'''

with open("path.json", "w") as f:
    json.dump(data, f)
# json serialization and desrialization
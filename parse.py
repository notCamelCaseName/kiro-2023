

filename = "small.json"

import json

f = open(filename,"r").read()
data = json.loads(f)

print(data.keys())

class Pos:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def __repr__(self):
        return f"({self.x}, {self.y} : {self.id})"

pos_v0 = tuple(data["general_parameters"]["main_land_station"].values())
pos_Vs = [Pos(k["x"], k["y"], k["id"]) for k in data["substation_locations"]]
print(pos_v0)
print(pos_Vs)
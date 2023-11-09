

filename = "small.json"

import json

_f = open(filename,"r").read()
_data = json.loads(_f)

class Pos:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def __repr__(self):
        return f"({self.x}, {self.y} : {self.id})"
    


_pos_v0 = _data["general_parameters"]["main_land_station"]
pos_v0 = Pos(_pos_v0["x"], _pos_v0["y"], 0)
Pmax = _data["general_parameters"]["main_land_station"]

pos_lst_Vs = [Pos(k["x"], k["y"], k["id"]) for k in _data["substation_locations"]]

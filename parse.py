

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
    
class Cable:
    def __init__(self, f_cost, var_cost, _id=None, proba_fail=None, rating=None):
        self.f_cost = f_cost
        self.var_cost = var_cost
        if _id:
            self.id = _id
        if proba_fail:
            self.proba_fail = proba_fail
        if rating:
            self.rating = rating
    
    def cost(self, length):
        return self.f_cost + length * self.var_cost



_pos_v0 = _data["general_parameters"]["main_land_station"]
pos_v0 = Pos(_pos_v0["x"], _pos_v0["y"], 0)
Pmax = _data["general_parameters"]["maximum_power"]
c0 = _data["general_parameters"]["curtailing_cost"]
cp = _data["general_parameters"]["curtailing_penalty"]
Cmax = _data["general_parameters"]["maximum_curtailing"]

pos_lst_Vs = [Pos(k["x"], k["y"], k["id"]) for k in _data["substation_locations"]]
cable_StaToSub = Cable(_data["general_parameters"]["fixed_cost_cable"],
                       _data["general_parameters"]["variable_cost_cable"])


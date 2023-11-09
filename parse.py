

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
        return f"Pos({self.x}, {self.y} : {self.id})"
    
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

    def __repr__(self):
        return f"Cable({self.f_cost} + l*{self.f_cost}, {self.proba_fail}, {self.rating} : {self.id})"
    
    def cost(self, length):
        return self.f_cost + length * self.var_cost
    
    def set_con(self, sub1, sub2):
        self.sub1 = sub1
        self.sub2 = sub2

class Sub:
    def __init__(self, cost, _id, proba_fail, rating):
        self.cost = cost
        self.id = _id
        self.proba_fail = proba_fail
        self.rating = rating

    def __repr__(self):
        return f"Sub({self.cost} +, {self.proba_fail}, {self.rating} : {self.id})"
    
    def set_cable(self, land_cable_type):
        self.land_cable_type = land_cable_type
    
    def set_pos(self, pos):
        self.pos = pos

class Turbine:
    def __init__(self, pos, _id):
        self.os = pos
        assert pos.id == _id
        self.id = _id

    def __repr__(self):
        return f"Turbine({self.pos} : {self.id})"
    
    def conect_station(self, station):
        self.station = station


_pos_v0 = _data["general_parameters"]["main_land_station"]
pos_v0 = Pos(_pos_v0["x"], _pos_v0["y"], 0)
Pmax = _data["general_parameters"]["maximum_power"]
c0 = _data["general_parameters"]["curtailing_cost"]
cp = _data["general_parameters"]["curtailing_penalty"]
Cmax = _data["general_parameters"]["maximum_curtailing"]

lst_pos_Sub = [Pos(k["x"], k["y"], k["id"]) for k in _data["substation_locations"]]

cable_SubToWind = Cable(_data["general_parameters"]["fixed_cost_cable"],
                       _data["general_parameters"]["variable_cost_cable"])

lst_sub = [Sub(k["cost"], k["id"], k["probability_of_failure"], k["rating"]) 
            for k in _data["substation_types"]]

lst_cable_HubToSub = [Cable(k["fixed_cost"], k["variable_cost"], 
                            k["id"], k["probability_of_failure"], k["rating"]) 
                            for k in _data["land_substation_cable_types"]]

lst_cable_HubToHub = [Cable(k["fixed_cost"], k["variable_cost"], 
                            k["id"]) 
                            for k in _data["substation_substation_cable_types"]]

lst_turbines = [Turbine(Pos(k["x"], k["y"], k["id"]), 
                            k["id"]) 
                            for k in _data["wind_turbines"]]


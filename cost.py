import json
import numpy as np

f = open('small.json')

data = json.load(f)

f.close()

def distance_substations(initial, id1, id2):
    first_subst = initial["substation_locations"][id1-1]
    second_subst = initial["substation_locations"][id2-1]
    return np.sqrt((first_subst["x"] - second_subst["x"])**2 + (first_subst["y"]-second_subst["y"])**2)

def distance_to_land(initial, id):
    turbine = initial["substation_locations"][id-1]
    base = initial["general_parameters"]["main_land_station"]
    return np.sqrt((turbine["x"] - base["x"])**2 + (turbine["y"] - base["y"])**2)

def distance_substation_turbine(initial, id_subst, id_turb):
    substation = initial["substation_locations"][id_subst-1]
    turbine = initial["wind_turbines"][id_turb-1]
    return np.sqrt((substation["x"] - turbine["x"])**2 + (substation["y"] - turbine["y"])**2)

def cost(initial, token):
    total_sum = 0

    for elem in token["substations"]:
        land_type = elem["land_cable_type"]
        sub_type = elem["substation_type"]
    
        total_sum += initial["land_substation_cable_types"][land_type-1]["fixed_cost"] + initial["land_substation_cable_types"][land_type-1]["variable_cost"]*distance_to_land(initial, land_type)
        total_sum += initial["substation_types"][sub_type-1]["cost"]

    for elem in token["substation_substation_cables"]: 
        id1 = elem["substation_id"]
        id2 = elem["other_substation_id"]
        cab_type = elem["cable_type"]
    
        total_sum += initial["substation_substation_cable_types"][cab_type-1]["fixed_cost"] + initial["substation_substation_cable_types"][cab_type-1]["variable_cost"]*distance_substations(initial, id1, id2)

    for elem in token["turbines"]:
        subst_id = elem["substation_id"]
        _id = elem["id"]

        total_sum += initial["general_parameters"]["fixed_cost_cable"] + initial["general_parameters"]["variable_cost_cable"]*distance_substation_turbine(initial, subst_id, _id)

    return total_sum



test = {
    "substations": [
        {
            "id": 1 ,
            "land_cable_type": 1 ,
            "substation_type": 1
        },
        {
            "id": 2 ,
            "land_cable_type": 2 ,
            "substation_type": 2
        }
    ],
    "substation_substation_cables": [
        {
            "substation_id": 1 ,
            "other_substation_id": 2 ,
            "cable_type": 2
        }
    ],
    "turbines": [
        {
            "id" : 1,
            "substation_id" : 1
        },
        {
            "id" : 2,
            "substation_id" : 1
        },
        {
            "id" : 3,
            "substation_id" : 2
        }
    ]
}

print(cost(data, test))

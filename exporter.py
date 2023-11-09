import json

def export_solution(substations, cables, turbines):
    res = {
        'substations': [
            {
                'id': sub.pos.id,
                'land_cable_type': sub.land_cable_type,
                'substation_type': sub.id
            } for sub in substations
        ],
        'substation_substation_cables': [
            {
                'substation_id': cable.sub1,
                'other_substation_id': cable.sub2,
                'cable_type': cable.id
            } for cable in cables
        ],
        'turbines': [
            {
                'id': turbine.id,
                'substation_id': turbine.sub.id
            } for turbine in turbines
        ]
    }

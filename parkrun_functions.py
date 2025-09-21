#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 11:38:25 2025

@author: chrisbutler
"""

import pandas as pd

  
def json_mapping(x):
    mapping_data = pd.read_json(x)
    mapping_data = pd.DataFrame(mapping_data['events']['features'])
    mapping_data['EventShortName'] = mapping_data['properties'].apply(lambda x: x['EventShortName'])
    mapping_data['coordinates'] = mapping_data['geometry'].apply(lambda x: x['coordinates'])
    mapping_data['lon'] = mapping_data['coordinates'].apply(lambda x: x[0])
    mapping_data['lat'] = mapping_data['coordinates'].apply(lambda x: x[1])
    mapping_data = mapping_data[['EventShortName', 'lon', 'lat']]
    return(mapping_data)
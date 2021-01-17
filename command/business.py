import geopandas as gpd
import json
import data.config

def suggest():
    homeDir = data.config.get_config('homeDir')
    demanda = gpd.read_file(homeDir+"\\data\\demanda.shp")
    top = demanda.groupby('demanda').demanda.count().sort_values(ascending=False)[:10]
    keys = top.keys()
    return json.dumps(list(keys))

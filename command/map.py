import subprocess
import geopandas as gpd
import os
import data.config

def render():
    homeDir = data.config.get_config('homeDir')
    database = data.config.get_config('database')
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile"'
    command = command+' "'+homeDir+'\\data\\logradouro.shp"'
    command = command+' MYSQL:"'+database['database']+',host='+database['host']+',user='+database['user']+',password='+database['password']+'" "logradouro"'
    subprocess.check_call(command, shell=True)
    logradouro = gpd.read_file(homeDir+"\\data\\logradouro.shp")
    base = logradouro.plot(color='black', edgecolor='black', linewidth=0.1)
    base.set_aspect(1)
    base.set_axis_off()
    chart = base.get_figure()
    filepath = homeDir + '/data/'+ 'mapa.jpg'
    chart.savefig(filepath, dpi=600)
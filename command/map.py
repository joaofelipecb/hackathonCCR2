import subprocess
import geopandas as gpd
import os
import data.config

def process():
    homeDir = data.config.get_config('homeDir')
    database = data.config.get_config('database')
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile"'
    command = command+' "'+homeDir+'\\data\\logradouro.shp"'
    command = command+' MYSQL:"'+database['database']+',host='+database['host']+',user='+database['user']+',password='+database['password']+'" "logradouro"'
    subprocess.check_call(command, shell=True)
    command = '"C:\\Program Files\\QGIS 3.16\\bin\\ogr2ogr.exe" -f "ESRI Shapefile"'
    command = command+' "'+homeDir+'\\data\\demanda.shp"'
    command = command+' MYSQL:"'+database['database']+',host='+database['host']+',user='+database['user']+',password='+database['password']+'" "demanda"'
    command = command+' -where "distancia > 10"'
    subprocess.check_call(command, shell=True)
    return ''
    
def render(business=False):
    homeDir = data.config.get_config('homeDir')
    database = data.config.get_config('database')
    logradouro = gpd.read_file(homeDir+"\\data\\logradouro.shp")
    demanda = gpd.read_file(homeDir+"\\data\\demanda.shp")
    if business == False:
        recorte = demanda
    else:
        recorte = demanda[demanda['demanda'] == business]
    base = logradouro.plot(color='black', edgecolor='black', linewidth=0.1)
    base.set_aspect(1)
    pontos = recorte.plot(ax=base, color='red', edgecolor='black', markersize=0.5, linewidth=0)
    pontos.set_aspect(1)
    base.set_axis_off()
    chart = base.get_figure()
    filepath = homeDir + '/data/'+ 'mapa.jpg'
    chart.savefig(filepath, dpi=600)
    return ''
    
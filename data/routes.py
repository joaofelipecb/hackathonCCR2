def get_route(name):
    routes = {}
    routes[''] = {'type': 'resource', 'path':'data/index.html'}
    routes['geolocalization'] = {'type': 'resource', 'path':'data/geolocalization.html'}
    routes['geolocalization2'] = {'type': 'resource', 'path':'data/geolocalization2.html'}
    routes['map'] = {'type': 'resource', 'path':'data/map.html'}
    routes['educationList'] = {'type': 'resource', 'path':'data/educationList.html'}
    routes['education'] = {'type': 'resource', 'path':'data/education.html'}
    routes['contract'] = {'type': 'resource', 'path':'data/contract.html'}
    routes['processMap'] = {'type': 'script', 'module':'control.map', 'function':'process'}
    routes['renderMap'] = {'type': 'script', 'module':'control.map', 'function':'render', 'parameters':['business']}
    routes['suggestBusiness'] = {'type': 'script', 'module':'control.business', 'function':'suggest'}
    return routes[name]
    
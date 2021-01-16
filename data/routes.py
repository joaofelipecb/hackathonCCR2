def get_route(name):
    routes = {}
    routes[''] = {'type': 'resource', 'path':'data/index.html'}
    routes['map'] = {'type': 'resource', 'path':'data/map.html'}
    routes['educationList'] = {'type': 'resource', 'path':'data/educationList.html'}
    return routes[name]
    
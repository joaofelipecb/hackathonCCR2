def get_route(name):
    routes = {}
    routes[''] = {'type': 'resource', 'path':'data/index.html'}
    return routes[name]
    
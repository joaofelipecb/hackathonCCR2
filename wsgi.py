import sys
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path)
import control.routes

def get_http_data(value):
    parts = value.split('&')
    parameters = {}
    for value in parts:
        pair = value.split('=')
        if len(pair) == 2:
            parameters[pair[0]] = pair[1]
    return parameters

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    get = env['QUERY_STRING']
    http_data = get_http_data(get)
    if 'route' not in http_data:
        route = ''
    else:
        route = http_data['route']
    result = control.routes.get_response(route,http_data)
    return [result.encode('ascii')]
    
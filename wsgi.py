import sys
sys.path.insert(0, "C:/xampp/htdocs/hackathonCCR2")
import control.routes

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    route = env['QUERY_STRING']
    result = control.routes.get_response(route)
    return [result.encode('ascii')]
    
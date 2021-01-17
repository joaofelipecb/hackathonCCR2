import data.routes
import data.config

def get_response(route):
    result = data.routes.get_route(route)
    if result['type'] == 'resource':
        homeDir = data.config.get_config('homeDir')
        file = open('c:\\xampp\\htdocs\\hackathonCCR2\\'+result['path'], "r")
        content = file.read()
        file.close()
        return content
    return "<html>not implemented</html>"

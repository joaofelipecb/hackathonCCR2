import data.routes

def get_response(route):
    result = data.routes.get_route(route)
    if result['type'] == 'resource':
        file = open('c:\\xampp\\htdocs\\hackathonCCR2\\'+result['path'], "r")
        content = file.read()
        file.close()
        return content
    return "<html>not implemented</html>"

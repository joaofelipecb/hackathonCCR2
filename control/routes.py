import data.routes
import data.config

def get_response(route):
    result = data.routes.get_route(route)
    if result['type'] == 'resource':
        homeDir = data.config.get_config('homeDir')
        file = open(homeDir+'/'+result['path'], "r")
        content = file.read()
        file.close()
        return content
    elif result['type'] == 'script':
        module = result['module']
        functionName = result['function']
        imported = __import__(module)
        parts = module.split('.')
        parts.pop(0)
        cursor = imported
        for part in parts:
            cursor = cursor.__getattribute__(part)
        function = cursor.__getattribute__(functionName)
        return function()        
    return "<html>not implemented</html>"

import data.routes
import data.config

def get_response(route, http_data):
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
        if 'parameters' in result:
            parameters = result['parameters']
        else:
            parameters = []
        imported = __import__(module)
        parts = module.split('.')
        parts.pop(0)
        cursor = imported
        for part in parts:
            cursor = cursor.__getattribute__(part)
        function = cursor.__getattribute__(functionName)
        arguments = {}
        for parameter in parameters:
            if parameter in http_data:
                arguments[parameter] = http_data[parameter]
        return function(**arguments)        
    return "<html>not implemented</html>"

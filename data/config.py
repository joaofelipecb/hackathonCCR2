import os 

def get_config(name):
    configs = {}
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.dirname(dir_path)
    configs['homeDir'] = dir_path
    configs['database'] = {}
    configs['database']['user'] = 'root'
    configs['database']['password'] = ''
    configs['database']['host'] = 'localhost'
    configs['database']['database'] = 'eivizinho'
    return configs[name]
    
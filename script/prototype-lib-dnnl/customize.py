from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    return {'return':0}

def postprocess(i):

    new_env = i['new_env']

    new_env['+C_INCLUDE_PATH'] = os.path.join(os.getcwd(), 'install', 'include')
    new_env['+CXX_INCLUDE_PATH'] = os.path.join(os.getcwd(), 'install', 'include')
    new_env['+LD_LIBRARY_PATH'] = os.path.join(os.getcwd(), 'install', 'lib')

    return {'return':0}

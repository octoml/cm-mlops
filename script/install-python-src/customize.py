from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    need_version = env.get('CM_VERSION','')
    if need_version == '':
        return {'return':1, 'error':'internal problem - CM_VERSION is not defined in env'}

    print (recursion_spaces + '    # Requested version: {}'.format(need_version))

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['+PATH'] = [os.path.join(os.getcwd(), 'install', 'bin')]
    env['+LD_LIBRARY_PATH'] = [os.path.join(os.getcwd(), 'install', 'lib')]
    env['+C_INCLUDE_PATH'] = [os.path.join(os.getcwd(), 'install', 'include')]

    return {'return':0}


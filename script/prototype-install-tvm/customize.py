from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    return {'return':0}

def postprocess(i):

    new_env = i['new_env']

    tvm_home = new_env['TVM_HOME']

    new_env['+PYTHONPATH'] = [os.path.join(tvm_home,'python')]

    return {'return':0}

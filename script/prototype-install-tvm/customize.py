from cmind import utils
import os

def postprocess(i):

    new_env = i['new_env']

    tvm_home = new_env['TVM_HOME']

    new_env['+PYTHONPATH'] = [os.path.join(tvm_home,'python')]

    return {'return':0}

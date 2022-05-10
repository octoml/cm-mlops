from cmind import utils
import os

def preprocess(i):

    automation = i['automation']
    cmind = automation.cmind

    new_env = i['new_env']
    new_state = i['new_state']

    os_info=i['os_info']

    # Update env variables
    new_env['CM_HOST_OS_TYPE']=os_info['platform']
    new_env['CM_HOST_OS_BITS']=os_info['bits']
    new_env['CM_HOST_PYTHON_BITS']=os_info['python_bits']

    new_state['os_info']=os_info

    if os.path.isfile('tmp-run-env.out'):
        os.remove('tmp-run-env.out')

    return {'return':0}


def postprocess(i):

    new_state = i['new_state']

    new_env = i['new_env']

    r = utils.load_txt(file_name='tmp-run-env.out',
                       check_if_exists = True)
    if r['return']>0: return r

    s = r['string'].split('\n')

    new_state['os_uname_machine']=s[0]
    new_state['os_uname_all']=s[1]

    new_env['CM_HOST_OS_MACHINE']=new_state['os_uname_machine']

    return {'return':0}

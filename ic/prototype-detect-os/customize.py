from cmind import utils
import os

def preprocess(i):

    cm = i['cmind']

    env = i['env']
    state = i['state']

    r = cm.access({'action':'get_host_os_info', 'automation':'utils,dc2743f8450541e3'})
    if r['return']>0: return r

    os_info=r['info']

    # Update env variables
    utils.update_dict_if_empty(env, 'CM_HOST_OS_TYPE', os_info['platform'])
    utils.update_dict_if_empty(env, 'CM_HOST_OS_BITS', os_info['bits'])
    utils.update_dict_if_empty(env, 'CM_HOST_PYTHON_BITS', os_info['python_bits'])

    state['os_info']=os_info

    if os.path.isfile('tmp-run.out'):
        os.remove('tmp-run.out')

    return {'return':0}


def postprocess(i):

    state = i['state']

    env = i['env']

    if not os.path.isfile('tmp-run.out'):
        return {'return':1, 'error':'tmp-run.out was not generated'}

    r = utils.load_txt(file_name='tmp-run.out')
    if r['return']>0: return r

    s = r['string'].split('\n')

    state['os_uname_machine']=s[0]
    state['os_uname_all']=s[1]

    utils.update_dict_if_empty(env, 'CM_HOST_OS_MACHINE', state['os_uname_machine'])

    return {'return':0}

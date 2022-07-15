from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']
    if env['CM_ENABLE_NUMACTL']:
        CM_RUN_PREFIX = "numactl " + env['CM_NUMACTL_MEMBIND'] + ' '
    else:
        CM_RUN_PREFIX = ''
    CM_RUN_PREFIX += env['CM_RUN_PREFIX']
    env['CM_RUN_PREIFX'] = CM_RUN_PREFIX

    CM_RUN_SUFFIX = (env['CM_REDIRECT_OUT'] + ' ') if env['CM_REDIRECT_OUT'] else ''
    CM_RUN_SUFFIX += env['CM_REDIRECT_ERR'] if env['CM_REDIRECT_ERR'] else ''
    env['CM_RUN_SUFFIX'] = env['CM_RUN_SUFFIX'] + CM_RUN_SUFFIX

    env['CM_RUN_COMMAND'] = CM_RUN_PREFIX + ' ' + env['CM_RUN_BINARY'] + ' ' + env['CM_RUN_SUFFIX']

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}

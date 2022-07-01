from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']


    host_os_bits = env['CM_HOST_OS_BITS']

    if os_info['platform'] != 'windows':
        host_os_machine = env['CM_HOST_OS_MACHINE'] # ABI

    cm = automation.cmind

    env['CM_TMP_FAIL_IF_NOT_FOUND'] = 'yes'

    return {'return':0}

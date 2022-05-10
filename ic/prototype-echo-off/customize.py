from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    # If windows, download here otherwise use run.sh
    if os_info['platform'] == 'windows':

        state = i['state']

        script_prefix = state.get('script_prefix',[])
        script_prefix.insert(0, '@echo off')
        state['script_prefix'] = script_prefix

    return {'return':0}

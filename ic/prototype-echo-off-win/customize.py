from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    new_state = i['new_state']

    # If windows, download here otherwise use run.sh
    if os_info['platform'] == 'windows':

        script_prefix = new_state.get('script_prefix',[])

        s='@echo off'
        if s not in script_prefix:
            script_prefix.insert(0, s)
        
        new_state['script_prefix'] = script_prefix

    # Test to skip next dependency
    #new_env = i['new_env']
    #new_env['CM_SKIP_SYS_UTILS']='YES'

    return {'return':0}

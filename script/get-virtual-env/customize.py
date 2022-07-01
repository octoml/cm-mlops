from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    automation = i['automation']

    recursion_spaces = i['recursion_spaces']

    env['CM_VIRTUAL_ENV_PATH'] = os.path.join(os.getcwd(), 'venv')

    s = 'Scripts' if os_info['platform'] == 'windows' else 'bin'
    env['CM_VIRTUAL_ENV_SCRIPTS_PATH'] = os.path.join(env['CM_VIRTUAL_ENV_PATH'], s)

    env['CM_TMP_PATH'] = env['CM_VIRTUAL_ENV_SCRIPTS_PATH']
    env['CM_TMP_FAIL_IF_NOT_FOUND'] = 'yes'

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']

    state = i['state']

    script_prefix = state.get('script_prefix',[])

    path_to_activate = os.path.join(env['CM_VIRTUAL_ENV_SCRIPTS_PATH'], 'activate')

    # If windows, download here otherwise use run.sh
    if os_info['platform'] == 'windows':
        path_to_activate += '.bat'

    s = os_info['run_bat'].replace('${bat_file}', path_to_activate)

    script_prefix.append(s)
    state['script_prefix'] = script_prefix

    return {'return':0}

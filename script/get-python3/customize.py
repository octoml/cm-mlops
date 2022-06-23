from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    recursion_spaces = i['recursion_spaces']

    file_name = 'python.exe' if os_info['platform'] == 'windows' else 'python3'

    r = i['automation'].find_artifact({'file_name': file_name,
                                       'env': env,
                                       'os_info':os_info,
                                       'default_path_env_key': 'PATH',
                                       'detect_version':True,
                                       'env_path_key':'CM_PYTHON_BIN_WITH_PATH',
                                       'run_script_input':i['run_script_input'],
                                       'recursion_spaces':i['recursion_spaces']})
    if r['return'] >0:
       if r['return'] == 16 and os_info['platform'] != 'windows':
           if env.get('CM_TMP_FAIL_IF_NOT_FOUND','').lower() == 'yes':
               return r

           print (recursion_spaces+'    # {}'.format(r['error']))

           # Attempt to run installer
           r = {'return':0, 'skip':True, 'script':{'tags':'install,python,src'}}

       return r


    found_path = r['found_path']

    if os_info['platform'] == 'windows':
        default_path_list = r['default_path_list']

        extra_path = os.path.join(os.path.dirname(found_path), 'Scripts')

        if extra_path not in default_path_list and extra_path+os.sep not in default_path_list:
            if '+PATH' not in env: env['+PATH'] = []
            env['+PATH'].append(os.path.join(os.path.dirname(found_path), 'Scripts'))

    # Check if include and lib:
    found_path_root = os.path.dirname(found_path)
    for x in [{'path': os.path.join(found_path_root, 'lib'), 'var':'LD_LIBRARY_PATH'},
              {'path': os.path.join(found_path_root, 'include'), 'var':'C_INCLUDE_PATH'}]:
        path = x['path']
        var = x['var']

        if os.path.isdir(path):
            default_path = os.environ.get(var, '').split(os_info['env_separator'])
            if path not in default_path and path+os.sep not in default_path:
                env['+'+var] = [path]

    env['CM_PYTHON_BIN']=file_name
    env['CM_PYTHON_BIN_WITH_PATH']=os.path.join(found_path, file_name)

    return {'return':0}


def postprocess(i):

    r = i['automation'].parse_version({'match_text': r'Python\s*([\d.]+)',
                                       'group_number': 1,
                                       'env_key':'CM_PYTHON_VERSION',
                                       'which_env':i['env']})
    if r['return'] >0: return r

    version = r['version']

    print (i['recursion_spaces'] + '      Detected version: {}'.format(version))

    return {'return':0, 'version':version}

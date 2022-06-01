from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    new_env = i['new_env']

    recursion_spaces = i['recursion_spaces']

    # If windows, download here otherwise use run.sh
    if os_info['platform'] == 'windows':
        file_name = 'clang.exe'
    else:
        file_name = 'clang'

    # Check paths to search
    path = env.get('CM_PATH','')

    default_path = False

    default_path_list = os.environ.get('PATH','').split(os_info['env_separator'])

    if path == '':
        path_list = default_path_list
        default_path = True
    else:
        print (recursion_spaces + '    # Requested path: {}'.format(path))
        path_list = path.split(os_info['env_separator'])

    # Prepare paths to search
    r = i['automation'].find_file_in_paths({'paths':path_list,
                                           'file_name':file_name, 
                                           'select':True,
                                           'recursion_spaces':i['recursion_spaces']})
    if r['return']>0: return r

    found_paths = r['found_paths']

    if len(found_paths)==0:
        return {'return':16, 'error':'{} not found'.format(file_name)}

    # Prepare env
    found_path = found_paths[0]

    path_bin = found_path

    if path_bin not in default_path_list:
        new_env['+PATH'] = [path_bin]

    full_path = os.path.join(found_path, file_name)
    print (recursion_spaces + '    # Found component: {}'.format(full_path))

    new_env['CM_LLVM_CLANG_BIN'] = file_name
    new_env['CM_LLVM_CLANG_BIN_WITH_PATH'] = full_path

    if os.path.isfile('tmp-ver.out'):
        os.remove('tmp-ver.out')

    return {'return':0}


def postprocess(i):

    new_env = i['new_env']

    r = utils.load_txt(file_name='tmp-ver.out', 
                       check_if_exists = True, 
                       split = True,
                       match_text = r'clang version\s*([\d.]+)',
                       fail_if_no_match = 'version was not detected')
    if r['return']>0: return r

    version = r['match'].group(1)

    print ('Detected version: {}'.format(version))

    new_env['CM_LLVM_CLANG_VERSION'] = version

    return {'return':0, 'version':version}

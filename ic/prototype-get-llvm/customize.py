from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    new_env = i['new_env']

    env_path = os.environ.get('PATH','')

    # If windows, download here otherwise use run.sh
    if os_info['platform'] == 'windows':
        file_name = 'clang.exe'
    else:
        file_name = 'clang'

    # Prepare paths to search
    r = i['automation'].find_file_in_paths({'paths':env_path.split(os_info['env_separator']), 
                                           'file_name':file_name, 
                                           'select':True,
                                           'recursion_spaces':i['recursion_spaces']})
    if r['return']>0: return r

    found_paths = r['found_paths']

    if len(found_paths)==0:
        return {'return':16, 'error':'component not detected'}

    # Prepare env
    found_path = found_paths[0]

    paths_bin = []

    path_bin = os.path.dirname(found_path)
    paths_bin.append(path_bin)

    new_env['+PATH'] = paths_bin

    clang_bin = file_name

    new_env['CM_LLVM_CLANG_BIN']=clang_bin
    new_env['CM_LLVM_CLANG_BIN_WITH_PATH']=os.path.join(found_path, clang_bin)

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

    return {'return':0}

from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']
    print(env)
    env['CM_C_COMPILER_FLAGS'] = " ".join(env['+CFLAGS']+ env['+CPPFLAGS'])
    env['CM_CXX_COMPILER_FLAGS'] = " ".join(env['+CXXFLAGS'] + env['+CPPFLAGS'])
    env['CM_F_COMPILER_FLAGS'] = " ".join(env['+FFLAGS'])
    env['CM_C_INCLUDE_FLAGS'] = " -I".join(env['+C_INCLUDE_DIR'])
    env['CM_CXX_INCLUDE_FLAGS'] = " -I".join(env['+CXX_INCLUDE_DIR'])
    env['CM_F_INCLUDE_FLAGS'] = " -I".join(env['+F_INCLUDE_DIR'])
    env['CM_C_LINKER_FLAGS'] = " ".join(env['+LDCFLAGS'])
    env['CM_CXX_LINKER_FLAGS'] = " ".join(env['+LDCXXFLAGS'])
    env['CM_F_LINKER_FLAGS'] = " ".join(env['+LDFFLAGS'])
    env['CM_LD_LIBRARY_PATHS'] = " -L".join(env['+LD_LIBRARY_PATH'])


    print(env)

    return {'return':0}

def postprocess(i):

    env = i['env']
    print(env)

    return {'return':0}

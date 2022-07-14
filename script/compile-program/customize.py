from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']
    
    env['CM_C_COMPILER_FLAGS'] = " ".join(env.get('+CFLAGS', []) + env.get('+CPPFLAGS', []))
    env['CM_CXX_COMPILER_FLAGS'] = " ".join(env.get('+CXXFLAGS', []) + env.get('+CPPFLAGS', []))
    env['CM_F_COMPILER_FLAGS'] = " ".join(env.get('+FFLAGS', []))
    env['CM_C_INCLUDE_FLAGS'] = " -I".join(env.get('+C_INCLUDE_DIR', []) + env.get('+CPATH', []))
    env['CM_CXX_INCLUDE_FLAGS'] = " -I".join(env.get('+CXX_INCLUDE_DIR', []) + env.get('+CPATH', []))
    env['CM_F_INCLUDE_FLAGS'] = " -I".join(env.get('+F_INCLUDE_DIR', []) + env.get('+CPATH', []))
    env['CM_C_LINKER_FLAGS'] = " ".join(env.get('+LDCFLAGS', []) + env.get('+LDFLAGS', []))
    env['CM_CXX_LINKER_FLAGS'] = " ".join(env.get('+LDCXXFLAGS', []) + env.get('+LDFLAGS', []))
    env['CM_F_LINKER_FLAGS'] = " ".join(env.get('+LDFFLAGS', []) + env.get('+LDFLAGS', []))
    env['CM_LD_LIBRARY_PATHS'] = " -L".join(env.get('+LD_LIBRARY_PATH', []))


    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}

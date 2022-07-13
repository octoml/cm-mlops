from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']
    env['+CFLAGS'] = env['CFLAGS'].split(" ") if "CFLAGS" in env else []
    env['+CPPFLAGS'] = env['CPPFLAGS'].split(" ") if "CPPFLAGS" in env else []
    env['+CXXFLAGS'] = env['CXXFLAGS'].split(" ") if "CXXFLAGS" in env else []
    env['+FFLAGS'] = env['FFLAGS'].split(" ") if "FFLAGS" in env else []
    env['+LDFLAGS'] = env['LDFLAGS'].split(" ") if "LDFLAGS" in env else []
    env['+LDCFLAGS'] = env['LDCFLAGS'].split(" ") if "LDCFLAGS" in env else []
    env['+LDCXXFLAGS'] = env['LDCXXFLAGS'].split(" ") if "LDCXXFLAGS" in env else []
    env['+LDFFLAGS'] = env['LDFFLAGS'].split(" ") if "LDFFLAGS" in env else []
    
    env['+C_INCLUDE_DIR'] = env['C_INCLUDE_DIR'].split(":") if "C_INCLUDE_DIR" in env else []
    env['+CXX_INCLUDE_DIR'] = env['CXX_INCLUDE_DIR'].split(":") if "CXX_INCLUDE_DIR" in env else []
    env['+F_INCLUDE_DIR'] = env['F_INCLUDE_DIR'].split(":") if "F_INCLUDE_DIR" in env else []
    if "CPATH" in env:
        env['+C_INCLUDE_DIR'] += env['CPATH'].split(":")
        env['+CXX_INCLUDE_DIR'] += env['CPATH'].split(":")

    if "FAST_COMPILER" in env:
        DEFAULT_COMPILER_FLAGS = "-O3"
        DEFAULT_LINKER_FLAGS = "-O3"
    else:
        DEFAULT_COMPILER_FLAGS = "-O2"
        DEFAULT_LINKER_FLAGS = "-O2"
    env['+CFLAGS'] += [DEFAULT_COMPILER_FLAGS]
    env['+CXXFLAGS'] += [DEFAULT_COMPILER_FLAGS]
    env['+FFLAGS'] += [DEFAULT_COMPILER_FLAGS]
    env['+LDFLAGS'] += [DEFAULT_LINKER_FLAGS, "-lm"]
    env['+LDCFLAGS'] +=  env['+LDFLAGS']
    env['+LDCXXFLAGS'] += env['+LDFLAGS']
    env['+LDFFLAGS'] += env['+LDFLAGS']


    if "LD_LIBRARY_PATH" in env:
        env['+LD_LIBRARY_PATH'] = env['LD_LIBRARY_PATH'].split(":")
    else:
        env['+LD_LIBRARY_PATH'] = []
    
    if env['CM_C_COMPILER_BIN'] == 'icc':
        if env['CM_CPUINFO_Vendor_ID'] == 'GenuineIntel':
            if int(env['CM_CPUINFO_CPU_family']) >= 0:
                env['+CFLAGS'] += ["-ipo"]
    if env['CM_C_COMPILER_BIN'] == 'gcc':
        if env['CM_CPUINFO_Vendor_ID'] == 'AMD':
            if int(env['CM_CPUINFO_CPU_family']) >= 0:
                env['+CFLAGS'] += ["-march=znver2", "-flto"]

    return {'return':0}

def postprocess(i):

    env = i['env']
    print(env)

    return {'return':0}

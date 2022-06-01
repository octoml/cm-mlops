from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    new_env = i['new_env']

    recursion_spaces = i['recursion_spaces']

    need_version = env.get('CM_NEED_VERSION','')
    if need_version == '':
        return {'return':1, 'error':'internal problem - CM_NEED_VERSION is not defined in env'}

    print (recursion_spaces + '    # Requested version: {}'.format(need_version))

    host_os_bits = new_env['CM_HOST_OS_BITS']

    if os_info['platform'] != 'windows':
        host_os_machine = new_env['CM_HOST_OS_MACHINE'] # ABI

    # Prepare package name
    if os_info['platform'] == 'darwin':
        package_name = 'clang+llvm-' + need_version + '-x86_64-apple-darwin.tar.xz'

    elif os_info['platform'] == 'windows':
        package_name = 'LLVM-' + need_version + '-win' + host_os_bits + '.exe'
    
    else:
       if host_os_machine.startswith('arm') or host_os_machine.startswith('aarch'):
          if host_os_bits=='64':
             package_name = 'clang+llvm-' + need_version + '-aarch64-linux-gnu.tar.xz'
          else:
             package_name = 'clang+llvm-' + need_version + '-armv7a-linux-gnueabihf.tar.xz'
       else:
          host_os_flavor = new_env['CM_HOST_OS_FLAVOR']

          host_os_version = new_env['CM_HOST_OS_VERSION']

          if 'debian' in host_os_flavor:
              return {'return':0, 'error':'debian is not supported yet'}

          else:
              default_os='18.04'

              if need_version == '10.0.1':
                  default_os = '16.04'

              elif need_version == '11.0.0':
                  default_os = '20.04'

              elif need_version == '11.0.1':
                  default_os = '16.04'
                  if host_os_version == '20.10':
                      default_os = '20.10'

              elif need_version == '12.0.0':
                  default_os = '16.04'
                  if host_os_version == '20.04' or host_os_version == '20.10':
                     default_os = '20.04'

              elif need_version == '12.0.1':
                  default_os = '16.04'
                  if host_os_version.startswith('18') or host_os_version.startswith('20'):
                     default_os = '18.04'

              elif need_version == '13.0.0':
                  default_os = '16.04'
                  if host_os_version.startswith('20'):
                     default_os = '20.04'

              elif need_version == '13.0.1':
                  default_os = '18.04'

              elif need_version == '14.0.0':
                  default_os = '18.04'

              package_name = 'clang+llvm-' + need_version + '-x86_64-linux-gnu-ubuntu-' + default_os + '.tar.xz'


    package_url = 'https://github.com/llvm/llvm-project/releases/download/llvmorg-' + need_version + '/' + package_name

    print (recursion_spaces + '    # Prepared package URL: {}'.format(package_url))

    print ('')
    print ('Downloading from {} ...'.format(package_url))

    cm = i['automation'].cmind

    r = cm.access({'action':'download_file', 
                   'automation':'utils,dc2743f8450541e3', 
                   'url':package_url})
    if r['return']>0: return r

    filename = r['filename'] # 'clang+llvm-12.0.0-x86_64-linux-gnu-ubuntu-20.04.tar.xz' # f['filename']

    new_env['CM_LLVM_PACKAGE'] = filename
    new_env['CM_PATH'] = os.getcwd() + '/bin'

    return {'return':0}

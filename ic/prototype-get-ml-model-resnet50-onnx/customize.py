from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    # Global env (do not record in an updated state of this component)
    env = i['env']
    # Changes in env by this components
    new_env = i['new_env']

    automation = i['automation']

    cm = automation.cmind

    path = os.getcwd()

    url = env['CM_PACKAGE_URL']

    print ('Downloading from {}'.format(url))

    r = cm.access({'action':'download_file', 
                   'automation':'utils,dc2743f8450541e3', 
                   'url':url})
    if r['return']>0: return r

    # Add to path
    new_env['CM_ML_MODEL_FILE']=r['filename']
    new_env['CM_ML_MODEL_FILE_WITH_PATH']=r['path']

    return {'return':0}

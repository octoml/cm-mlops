from cmind import utils
import os

lscpu_out = 'tmp-lscpu.out'

def preprocess(i):

    if os.path.isfile(lscpu_out):
        os.remove(lscpu_out)

    return {'return':0}


def postprocess(i):

    state = i['state']

    env = i['env']

    if not os.path.isfile(lscpu_out):
        return {'return':1, 'error':'{} was not generated'.format(lscpu_out)}

    r = utils.load_txt(file_name=lscpu_out)
    if r['return']>0: return r

    ss = r['string']

    state['cpu_info_raw'] = ss

    print ('')
    for s in ss.split('\n'):
        print (s)

    return {'return':0}

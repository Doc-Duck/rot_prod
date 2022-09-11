import pandas as pd
import numpy as np
from lmfit.models import Model
from scipy.interpolate import interp1d


def spectr(consts, k, b, alpha, beta):
    return k*consts[0] + b + alpha*consts[1] + beta*consts[2]


def get_hb_val(spectra_path, light_path, dark_path, hb_path): # absolute path to table with spectra
    spectra = pd.read_csv(spectra_path, names=['WL', 'val'], skiprows=[0])
    light = pd.read_csv(light_path, names=['WL', 'val'], skiprows=[0])
    dark = pd.read_csv(dark_path, names=['WL', 'val'], skiprows=[0])

    hb = pd.read_csv(hb_path, sep='\t')
    oxy_hem = interp1d(hb['lambda'], hb['Hb02'])
    hem = interp1d(hb['lambda'], hb['Hb'])
    spectra['dark'] = dark['val'].copy()
    spectra['light'] = light['val'].copy()
    spectra['num'] = spectra['val'] - spectra['dark']
    # spectra['num'] = spectra['num'].apply(lambda x: x if x > 0 else 1)
    spectra['denum'] = spectra['light'] - spectra['dark']
    spectra['R'] = spectra['num'] / spectra['denum']
    spectra['OD'] = -np.log(spectra['R']).rolling(window=20, center=True).mean()
    spectra = spectra[(spectra['WL'] > 475) & (spectra['WL'] < 650)]
    interp_hb = pd.DataFrame(zip(spectra['WL'], oxy_hem(spectra['WL']), hem(spectra['WL'])),
                             columns=['WL', 'Hb02', 'Hb'])
    scale = 100000
    ox_hb, des_hb = interp_hb['Hb02'] / scale, interp_hb['Hb'] / scale
    lam = interp_hb['WL']
    md = Model(spectr)
    params = md.make_params(k=0, b=0, alpha=0.6, beta=0.9)
    res = md.fit(spectra['OD'].to_numpy(), consts=(lam.values, ox_hb, des_hb), params=params)

    return res.values['alpha']/(res.values['alpha'] + res.values['beta']), res.values['alpha'] + res.values['beta']


"""
Usage:
oxygen, sun_hem = get_hb_val(spectra_path, light_path, dark_path, hb_path, )
Another example:
print(get_hb_val(spectra_path='/home/atemiy/optic/occlusion/finger_occlusion_kazim_1_OceanOptics-MAYP11400_reflected_18_34_29_772.csv',
                 light_path='/home/atemiy/optic/occlusion/finger_occlusion_dinislam_repeat1_OceanOptics-MAYP11400_light_18_21_29_048.csv',
                 dark_path='/home/atemiy/optic/occlusion/finger_occlusion_dinislam_repeat1_OceanOptics-MAYP11400_dark_18_21_21_407.csv',
                 hb_path='Hb_spectra.tsv'))
"""
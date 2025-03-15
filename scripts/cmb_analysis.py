# scripts/cmb_analysis.py
import h5py
import numpy as np
from scipy.stats import kurtosis  # Example analysis tool

def analyze_cmb_non_gaussianity(h5_path):
    """Compute CMB bispectrum/non-Gaussianity from TFM initial conditions."""
    # Load data from HDF5
    with h5py.File(h5_path, 'r') as f:
        T_fluctuations = f['T_fluctuations'][:]
        phi_initial = f['phi_initial'][:]
        alpha = f.attrs['alpha']
        beta = f.attrs['beta']
    
    # Compute non-Gaussian statistics (example: kurtosis)
    f_nl = kurtosis(T_fluctuations.flatten()) * beta**2  # Simplified model
    return f_nl

if __name__ == "__main__":
    f_nl = analyze_cmb_non_gaussianity('data/cmb_initial_conditions.h5')
    print(f"TFM-predicted f_NL: {f_nl:.3f}")

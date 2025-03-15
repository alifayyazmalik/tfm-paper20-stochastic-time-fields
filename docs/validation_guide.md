# Validation Guide  
Reproduce key results from **The Stochastic Architecture of Time Fields** (Paper #20).  

---

## 1. Ornstein-Uhlenbeck (OU) Time-Field Trajectories  
**Script:** `scripts/ou_simulations.py`  
**Output:** `figures/OU_trajectories.png`  
**Steps:**  
1. Simulate trajectories with parameters from Figure 1:  
   ```bash  
   python scripts/ou_simulations.py --alpha 0.5 --beta 1.0 --steps 1000  
   python scripts/ou_simulations.py --alpha 2.0 --beta 1.0 --steps 1000  
   ```
Compare the output plot to Figure 1 in the paper.  
Higher α (orange curve) should show faster damping.  

---

## 2. Fractal Cosmic Web (Diffusion-Limited Aggregation)  
**Script:** `scripts/fractal_web.py`  
**Output:** `figures/DLA_fractal.png`  
**Steps:**  
1. Generate a cosmic web fractal:  
   ```bash  
   python scripts/fractal_web.py --size 500 --particles 5000  
   ```
Compare the void/filament structure to Figure 2 and SDSS/BOSS observations.  

---

## 3. Quantum Entanglement (CHSH Violation)  
**Script:** `scripts/entanglement_model.py`  
**Output:** Terminal print of CHSH parameter S.  
**Steps:**  
1. Run the entanglement noise model:  
   ```bash  
   python scripts/entanglement_model.py --rho 0.99  
   ```
Verify that S ≈ 2.8 (exceeding the classical Bell limit of 2.0).  

---

## 4. CMB Non-Gaussianity \( f_{NL} \)  
**Script:** `scripts/cmb_analysis.py`  
**Data:** `data/cmb_parameters.h5`  
**Steps:**  
1. Compute the bispectrum from TFM time-field fluctuations:  
   ```bash  
   python scripts/cmb_analysis.py --input data/cmb_parameters.h5  
   ```
Confirm output matches the predicted \( f_{NL} \sim 0.02 \) (Paper: Section 5.2).  

---

## 5. LIGO Noise Floor \( S(f) \propto f^{-3/2} \)  
**Script:** `scripts/ligo_noise.py`  
**Output:** `figures/ligo_noise_psd.png`  
**Steps:**  
1. Generate the TFM-predicted noise spectrum:  
   ```bash  
   python scripts/ligo_noise.py --fmin 100 --fmax 1000  
   ```
Plot the power spectral density (PSD) and check the slope aligns with \( -3/2 \).  

---

## Notes  
- **Dependencies:** Install requirements via `pip install -r requirements.txt`.  
- **Data Sources:**  
  - SDSS/BOSS galaxy surveys: [SDSS](https://www.sdss.org/)  
  - Planck 2018 CMB: [Planck Archive](https://pla.esac.esa.int/)  
  - LIGO O3 noise curves: [GWOSC](https://gwosc.org/)  
- **Issues?** Open a GitHub ticket or contact [alifayyaz@live.com](mailto:alifayyaz@live.com).  

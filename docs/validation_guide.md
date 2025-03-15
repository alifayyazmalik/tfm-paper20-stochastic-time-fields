# Validation Guide

## 1. **Reproduce Figure 1**
```bash
python scripts/ou_simulations.py --alpha 0.5 --beta 1.0
```

## 2. **Compare with Planck 2018 Data**
```python
from scripts import cmb_analysis
cmb_analysis.compare_planck('data/cmb_parameters.h5')
```

---

## 3. **Paper Modifications**  
### **Add "Code and Data Availability" Section**  
Insert after the Conclusion:  
```latex
%===========================================================
\section{Code and Data Availability}
\label{sec:code_data}

All code and datasets are archived at:  
\url{https://github.com/YourUsername/tfm-paper20-stochastic-time-fields}.  
This includes:  
\begin{itemize}
  \item Ornstein-Uhlenbeck time-field simulations (Section~\ref{sec:stochastic})
  \item Fractal cosmic web generator (Section~\ref{sec:fractalwebs})
  \item Quantum entanglement noise model (Appendix~\ref{sec:appendixB})
\end{itemize}

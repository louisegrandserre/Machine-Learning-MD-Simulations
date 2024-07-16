# Phonon Mode Calculation Tutorial using VASP and Phonopy

In this directory, a tutorial is provided for calculating phonon modes using VASP with Phonopy. To perform this calculation, follow these steps outlined on the Phonopy documentation at [Phonopy VASP DFPT Tutorial](https://phonopy.github.io/phonopy/vasp-dfpt.html):

1. **Create Supercells:**
   Generate supercells of the unit cell structure suitable for phonon calculations.

2. **Run DFT Calculation with INCAR Provided:**
   Perform Density Functional Theory (DFT) calculations using VASP with the provided INCAR file. Adjust parameters as necessary for your specific system and calculation requirements.

3. **Analyze Phonon Modes:**
   Deduce phonon modes and analyze the phonon spectrum based on the results obtained from the DFT calculations with the calcul-phonon_modes.py script.

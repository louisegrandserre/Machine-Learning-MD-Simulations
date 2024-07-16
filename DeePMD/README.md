# DeePMD for Molecular Dynamics Simulations

This directory contains scripts and files for utilizing DeePMD (Deep Potential Molecular Dynamics) for simulating water molecules. The scripts provided here facilitate data preparation, model training, and comparison with DFT calculations, along with phonon calculations using Phonolammps and Phonopy.

## Scripts and Files:

### `prepare_deepmd_data.py`:
- This script prepares input data for DeePMD using outputs from VASP calculations.

### `input.json`:
- Configuration file used for training the DeePMD model.
- Modify parameters and hyperparameters for specific training setups (here fited for water).

### `compare_energies.py` and `compare_forces.py`:
- Scripts to compare energies and forces predicted by the DeePMD force field against DFT-calculated values.

### `rmse.py`:
- Script to compute Root Mean Squared Error (RMSE) loss during training steps.

### `phonon/` Directory:
- Contains a script to calculate phonon Density of States (DOS) and band structures: `calcul_phonon_modes`, using Phonolammps and Phonopy.

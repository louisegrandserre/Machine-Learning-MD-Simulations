"""
Python script for preparing DeePMD data from Density Functional Theory (DFT) calculations conducted using VASP.
Data extraction is based on information parsed from vasprun.xml.
This script is designed to handle 800 steps of Ab Initio Molecular Dynamics (AIMD) data.
"""

import dpdata
import numpy as np

# load data of vasprun
data = dpdata.LabeledSystem("chemin_vers_vasprun.xml")
print("# the data contains %d frames" % len(data))

# random choose 100 index for validation_data
rng = np.random.default_rng()
index_validation = rng.choice(800, size=100, replace=False)

# other indexes are training_data
index_training = list(set(range(800)) - set(index_validation))
data_training = data.sub_system(index_training)
data_validation = data.sub_system(index_validation)

# all training data put into directory:"training_data"
data_training.to_deepmd_npy("00.data/training_data")

# all validation data put into directory:"validation_data"
data_validation.to_deepmd_npy("00.data/validation_data")

print("# the training data contains %d frames" % len(data_training))
print("# the validation data contains %d frames" % len(data_validation))

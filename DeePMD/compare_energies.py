#Script to plot Energy predicted by the DeePMD force field with respect to the energy predicted by DFT calculations

import dpdata
from sklearn.metrics import mean_squared_error
from sklearn.metrics import root_mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

training_systems = dpdata.LabeledSystem(
    "./00.data/training_data", fmt="deepmd/npy"
)
predict = training_systems.predict("./01.train/graph.pb")

rmse_energies = np.sqrt(mean_squared_error(training_systems["energies"], predict["energies"]))

plt.figure(figsize=(8, 6))
plt.scatter(training_systems["energies"], predict["energies"])
x_range = np.linspace(plt.xlim()[0], plt.xlim()[1])
plt.plot(x_range, x_range, "r--", linewidth=0.25)

for energy, pred_energy, rmse_energy in zip(training_systems["energies"], predict["energies"], [rmse_energies]*len(training_systems["energies"])):
    plt.fill_between([energy], pred_energy - rmse_energy, pred_energy + rmse_energy, color='blue', alpha=0.3)

plt.xlabel("Energy of DFT")
plt.ylabel("Energy predicted by deep potential")
plt.title("Comparison of Energies")
plt.grid(True)
plt.savefig('comp_with_rmse.png')

#Script to plot the forces predicted by the DeePMD force field compared to the forces predicted by DFT calculations

import dpdata

training_systems = dpdata.LabeledSystem(
    "./00.data/training_data", fmt="deepmd/npy"
)
predict = training_systems.predict("./01.train/graph.pb")

import matplotlib.pyplot as plt
import numpy as np

plt.scatter(training_systems["forces"], predict["forces"])

x_range = np.linspace(plt.xlim()[0], plt.xlim()[1])

plt.plot(x_range, x_range, "r--", linewidth=0.25)
plt.xlabel("Force of DFT")
plt.ylabel("Force predicted by deep potential")
plt.plot()
plt.grid(True)
plt.savefig('comp_force.png')
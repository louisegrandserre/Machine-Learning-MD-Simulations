import phonopy
from phonopy.phonon.band_structure import get_band_qpoints_and_path_connections

path = [[[0, 0, 0], [0.5, 0, 0.5], [0.625, 0.25, 0.625]],
        [[0.375, 0.375, 0.75], [0, 0, 0], [0.5, 0.5, 0.5], [0.5, 0.25, 0.75]]]
labels = ["$\\Gamma$", "X", "U", "K", "$\\Gamma$", "L", "W"]
qpoints, connections = get_band_qpoints_and_path_connections(path, npoints=51)
phonon = phonopy.load("phonopy.yaml")
phonon.run_band_structure(qpoints, path_connections=connections, labels=labels)
fig = phonon.plot_band_structure()
fig.savefig("bandes.png")

# To plot DOS next to band structure
phonon.run_mesh([20, 20, 20])
##phonon.run_total_dos()
#fig = phonon.plot_band_structure_and_dos()
#fig.savefig("dos.png")

# To plot PDOS next to band structure
#phonon.run_mesh([20, 20, 20], with_eigenvectors=True, is_mesh_symmetry=False)
#phonon.run_projected_dos()
#fig = phonon.plot_band_structure_and_dos(pdos_indices=[[0], [1]])
#fig.savefig("pdos.png")

phonon.set_mesh([20, 20, 20])
phonon.set_total_DOS()
fig = phonon.plot_total_DOS()
fig.savefig('total_DOS.png')

phonon.set_thermal_properties()
fig = phonon.plot_thermal_properties()
fig.savefig('th_properties.png')


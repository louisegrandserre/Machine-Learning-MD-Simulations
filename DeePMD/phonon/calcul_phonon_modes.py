from phonolammps import Phonolammps
import matplotlib.pyplot as plt

phlammps = Phonolammps('input.lammps',
                       supercell_matrix=[[2, 0, 0],
                                         [0, 2, 0],
                                         [0, 0, 2]])

unitcell = phlammps.get_unitcell()
force_constants = phlammps.get_force_constants()
supercell_matrix = phlammps.get_supercell_matrix()

from phonopy import Phonopy
phonon = Phonopy(unitcell,
                 supercell_matrix)

phonon.set_force_constants(force_constants)
phonon.set_mesh([20, 20, 20])

phonon.set_total_DOS()
fig = phonon.plot_total_DOS()
fig.savefig('total_DOS.png')

phonon.set_thermal_properties()
fig = phonon.plot_thermal_properties()
fig.savefig('th_properties.png')

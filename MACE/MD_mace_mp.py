#Script to run a MD simulation with MACE-MP-0

from mace.calculators import mace_mp
from ase.md.nvtberendsen import NVTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
from ase.io import Trajectory
from ase.io import read, write
from ase.io.trajectory import Trajectory

macemp = mace_mp() 
atoms = read('POSCAR')
atoms.calc = macemp

T_init = 350
MaxwellBoltzmannDistribution(atoms, T_init * units.kB)

dyn = NVTBerendsen(atoms, 0.5 * units.fs, T_init, taut=0.5)
traj = Trajectory('mace_md.traj', 'w', atoms)
dyn.attach(traj.write, interval=1)
n_steps = 800 
dyn.run(n_steps)

traj = read('mace_md.traj', index=':')
write('mace_md.xyz', traj)

#https://jageo.github.io/TutorialAtomate2Forcefields/phonon.html
#Script to plot phonon DOS and band structures for VASP, MACE-MP-0 and CHGNET using Atomate2
from atomate2.forcefields.flows.phonons import PhononMaker
from pymatgen.core.structure import Structure
import atomate2.forcefields.jobs as ff_jobs
from pymatgen.core.composition import Element, Composition

struct = Structure.from_file('POSCAR')


###### MACE ######

phonon_flow_mace = PhononMaker(min_length=15.0, store_force_constants=False,
                          bulk_relax_maker=ff_jobs.MACERelaxMaker(relax_kwargs={"fmax": 0.00001}),
                          phonon_displacement_maker=ff_jobs.MACEStaticMaker(),
                          static_energy_maker=None).make(structure=struct)

from jobflow import run_locally

run_locally(phonon_flow_mace, create_folders=True)

from pymatgen.phonon.bandstructure import PhononBandStructureSymmLine
from pymatgen.phonon.dos import PhononDos
from pymatgen.phonon.plotter import PhononBSPlotter, PhononDosPlotter
from jobflow import SETTINGS

store = SETTINGS.JOB_STORE
store.connect()

result_mace = store.query_one(
    {"name": "generate_frequencies_eigenvectors"},
    properties=[
        "output.phonon_dos",
        "output.phonon_bandstructure",
    ],
    load=True,
    sort={"completed_at": -1} # to get the latest computation
)

ph_bs_mace = PhononBandStructureSymmLine.from_dict(result_mace['output']['phonon_bandstructure']) # get pymatgen bandstructure object
ph_dos_mace = PhononDos.from_dict(result_mace['output']['phonon_dos']) # get pymatgen phonon dos object




##### CHGNET #####

from atomate2.forcefields.flows.phonons import PhononMaker
from pymatgen.core.structure import Structure


phonon_flow_CHGNET = PhononMaker(min_length=15.0, store_force_constants=False).make(structure=struct) # CHGNET is the default so dont need to specify it


from jobflow import run_locally

run_locally(phonon_flow_CHGNET, create_folders=True)

from pymatgen.phonon.bandstructure import PhononBandStructureSymmLine
from pymatgen.phonon.dos import PhononDos
from pymatgen.phonon.plotter import PhononBSPlotter, PhononDosPlotter
from jobflow import SETTINGS

store = SETTINGS.JOB_STORE
store.connect()

result_CHGNET = store.query_one(
    {"name": "generate_frequencies_eigenvectors"},
    properties=[
        "output.phonon_dos",
        "output.phonon_bandstructure",
    ],
    load=True,
    sort={"completed_at": -1} # to get the latest computation
)

ph_bs_CHGNET = PhononBandStructureSymmLine.from_dict(result_CHGNET['output']['phonon_bandstructure']) # get pymatgen bandstructure object
ph_dos_CHGNET = PhononDos.from_dict(result_CHGNET['output']['phonon_dos']) # get pymatgen phonon dos object

##### VASP #####


from atomate2.vasp.flows.phonons import PhononMaker
from pymatgen.core.structure import Structure
#import atomate2.vasp.jobs as vasp_jobs
from atomate2.vasp.jobs.core import RelaxMaker, StaticMaker

from jobflow import run_locally
from pymatgen.phonon.bandstructure import PhononBandStructureSymmLine
from pymatgen.phonon.dos import PhononDos
from atomate2.vasp.sets.core import RelaxSetGenerator
from atomate2.vasp.sets.core import StaticSetGenerator


struct = Structure(
    lattice=[[0, 2.73, 2.73], [2.73, 0, 2.73], [2.73, 2.73, 0]],
    species=["Si", "Si"],
    coords=[[0, 0, 0], [0.25, 0.25, 0.25]],
)

#rlx_gen = RelaxSetGenerator(user_incar_settings={'ISMEAR':0,'LVTOT':None})
static_gen = StaticSetGenerator(user_incar_settings={'ISMEAR':0,'LVTOT':None})
#static_gen = StaticSetGenerator(auto_ismear = True)

#get_supercell_size_kwargs = {"max": 2} #added
phonon_flow_vasp = PhononMaker(
    min_length=15.0, 
    store_force_constants=True,
    bulk_relax_maker=RelaxMaker(),
    phonon_displacement_maker = StaticMaker(input_set_generator = static_gen),
    static_energy_maker=None
).make(structure=struct, supercell_matrix = [[2.0,0.0,0.0],[0.0,2.0,0.0],[0.0,0.0,2.0]] )

run_locally(phonon_flow_vasp, create_folders=True)

from pymatgen.phonon.plotter import PhononBSPlotter, PhononDosPlotter
from jobflow import SETTINGS

store = SETTINGS.JOB_STORE
store.connect()

result_vasp = store.query_one(
    {"name": "generate_frequencies_eigenvectors"},
    properties=[
        "output.phonon_dos",
        "output.phonon_bandstructure",
    ],
    load=True,
    sort={"completed_at": -1}  
)

ph_bs_vasp = PhononBandStructureSymmLine.from_dict(result_vasp['output']['phonon_bandstructure'])
ph_dos_vasp = PhononDos.from_dict(result_vasp['output']['phonon_dos'])


######PLOT####

# initialize dos plotter and visualize dos plot
import matplotlib.pyplot as plt
import numpy as np


dos_plot = PhononDosPlotter()
dos_plot.add_dos(label='MACE', dos=ph_dos_mace, color='blue', linestyle='--')
dos_plot.add_dos(label='CHGNET', dos=ph_dos_CHGNET, color='green', linestyle='--')
dos_plot.add_dos(label='DFT', dos=ph_dos_vasp, color='red', linestyle='-')
dos = dos_plot.get_plot()
dos.figure.tight_layout()
dos.figure.savefig('dos_MACEvsCHGNETvsVASP', bbox_inches='tight')

bs_plot_mace = PhononBSPlotter(bs=ph_bs_mace, label='MACE')
bs_plot_chgnet = PhononBSPlotter(bs=ph_bs_CHGNET, label='CHGNET')
bs_plot_dft = PhononBSPlotter(bs=ph_bs_vasp, label='DFT')

all_bs = {'CHGNET':bs_plot_chgnet,'MACE':bs_plot_mace }
bs = bs_plot_dft.plot_compare(other_plotter = all_bs,colors=['red', 'green', 'blue'],legend_kwargs={'loc': 'upper right'},
    units='thz',
)
bs.figure.tight_layout() 
bs.figure.savefig('bs_MACEvsCHGNETvsVASP', bbox_inches='tight')

dos_plot = PhononDosPlotter()
dos_plot.add_dos(label='MACE', dos=ph_dos_mace, color='blue', linestyle='--')
dos_plot.add_dos(label='DFT', dos=ph_dos_vasp, color='red', linestyle='-')
dos = dos_plot.get_plot()
dos.figure.tight_layout()
dos.figure.savefig('dos_MACEvsVASP', bbox_inches='tight')

bs_plot_dft = PhononBSPlotter(bs=ph_bs_vasp, label='DFT')
bs_plot_mace = PhononBSPlotter(bs=ph_bs_mace, label='MACE')
bs_plot_dft.plot_compare(
    other_plotter={'MACE': bs_plot_mace},
    colors=['red','blue'],  
    legend_kwargs={'loc': 'upper right'},
    units='thz',
)
bs.figure.tight_layout() 
bs.figure.savefig('bs_DFTvsMACE.png', bbox_inches='tight')

dos_plot = PhononDosPlotter()
dos_plot.add_dos(label='DFT', dos=ph_dos_vasp, color='red', linestyle='-')
dos = dos_plot.get_plot()
dos.figure.tight_layout()
dos.figure.savefig('dos_VASP', bbox_inches='tight')

bs_plot_dft = PhononBSPlotter(label='DFT', bs=ph_bs_vasp, color='red', linestyle='-')
bs_plot_dft.get_plot(color='red', linestyle='-')
bs.figure.tight_layout()
bs.figure.savefig('bs_DFT.png', bbox_inches='tight')



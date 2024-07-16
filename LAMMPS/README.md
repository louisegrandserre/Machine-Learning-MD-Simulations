# Molecular Dynamics (MD) Simulation and RDF Calculation with LAMMPS

This directory contains an LAMMPS input file (`input.lammps`) that performs Molecular Dynamics (MD) simulations for water molecules and calculates the Radial Distribution Function (RDF).

## Script Description:

### `input.lammps`:
- This LAMMPS input script executes MD simulations for water molecules.
- It computes the Radial Distribution Function (RDF) based on the trajectory generated during MD simulation.

### `submit_lammps.sh`:
- Use this script to submit the LAMMPS job for execution on your computing environment.


## Usage:

1. **Execution:**
   - Place `input.lammps` in your LAMMPS working directory.
   - Run the simulation using the submit_lammps.sh

2. **Modification:**
   - Modify `input.lammps` to adjust simulation parameters, atom types, and RDF computation settings for different molecular systems.

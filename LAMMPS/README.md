# Molecular Dynamics (MD) Simulation and RDF Calculation with LAMMPS

This directory contains an LAMMPS input file (`input.lammps`) that performs Molecular Dynamics (MD) simulations for water molecules and calculates the Radial Distribution Function (RDF).

## Script Description:

### `input.lammps`:
- This LAMMPS input script executes MD simulations for water molecules.
- It computes the Radial Distribution Function (RDF) based on the trajectory generated during MD simulation.

## Usage:

1. **Setup:**
   - Ensure LAMMPS is installed and configured on your system.

2. **Execution:**
   - Place `input.lammps` in your LAMMPS working directory.
   - Run the simulation using the submit_lammps.sh

3. **Output:**
   - The script will output trajectory files and RDF data suitable for analysis.

4. **Modification:**
   - Modify `input.lammps` to adjust simulation parameters, atom types, and RDF computation settings for different molecular systems.

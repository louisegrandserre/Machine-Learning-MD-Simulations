#!/bin/bash
#SBATCH --account=def-bevankir
#SBATCH --gpus-per-node=2
#SBATCH --cpus-per-task=6
#SBATCH --mem=10GB # Memoire par noeud
#SBATCH --time=00-06:00 # time (DD-HH:MM)
#SBATCH --job-name H2O # Nom du job
#SBATCH --output H2O.out # Nom de l'output de slurm

Project=""
MyDir=""

cd $MyDir/$Project
echo "Current working directory: $PWD"

module load StdEnv/2023  intel/2023.2.1  lammps-omp/20230802

lmp < input.lammps > lammps_output.txt


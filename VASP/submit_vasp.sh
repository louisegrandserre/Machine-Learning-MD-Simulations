#!/bin/bash
#SBATCH --account=def-bevankir
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=10GB # Memoire par noeud
#SBATCH --time=00-02:00 # time (DD-HH:MM)
#SBATCH --job-name AIMD # Nom du job
#SBATCH --output AIMD.out # Nom de l'output de slurm

# Definir les dossiers

WorkDir="" # Nom du dossier de travail
MainDir="" # Nom de l'emplacement du dossier de travail
# Aller dans le dossier
cd $MainDir/$WorkDir

# Charger les modules pour vasp
module load nixpkgs/16.09 intel/2019.3  intelmpi/2019.3.199

# Lancer VASP
srun /home/USER/vasp_std > vasp.log 2>&1

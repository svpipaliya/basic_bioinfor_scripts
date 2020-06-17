#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --account=def-dacks
#SBATCH --mem-per-cpu=20000M
#SBATCH --ntasks=16
#SBATCH --mail-user=pipaliya@ualberta.ca
#SBATCH --job-name=test_RAxML
#SBATCH --output=test_RAxML_out

module load intel/2018.3
module load openmpi/3.1.2
module load raxml/8.2.11

#raxml using MPI, nthreads set to 8 (refer to RAxML on parallel processing in manual for alternative), model LG4X using gamma distribution, seed setting random
mpirun -n 8 raxmlHPC-MPI -f d -m PROTGAMMALG4X -s example-phy -# 100 -p 12345 -b 12345 -n MultipleBootstrap

##End Script

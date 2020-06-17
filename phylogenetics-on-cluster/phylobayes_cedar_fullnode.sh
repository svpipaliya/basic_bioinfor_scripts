#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --account=def-dacks
#SBATCH --nodes=1
#SBATCH --ntasks=32
#SBATCH --mem=0
#SBATCH --mail-user=pipaliya@ualberta.ca
#SBATCH --job-name=test_pb
#SBATCH --output=test_pb.out

module load intel/2018.3
module load openmpi/3.1.2
module load phylobayes-mpi/20180420

#phylobayes on MPI, nthreads set to 8 (refer to PB manual to alternative options), CAT-GTR model (use LG if CAT not necessary)
mpirun -n 8 pb_mpi -d example.phy -cat -gtr example_out

##End Script

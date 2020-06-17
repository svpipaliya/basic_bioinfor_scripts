#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --account=def-dacks
#SBATCH --mem-per-cpu=20000M
#SBATCH --ntasks=16
#SBATCH --mail-user=pipaliya@ualberta.ca
#SBATCH --job-name=test_IQTREE
#SBATCH --output=test_IQTREE_out

module load gcc/7.3.0
module load intel/2018.3
module load iq-tree/1.6.12

#simple ultrafastboostrapping - refer to IQTREE manual for additional parameter options
iqtree -nt AUTO -s example.phy -m MFP -bb 1000 

##End Script

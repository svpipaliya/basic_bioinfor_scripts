#!/bin/bash
#
#SBATCH -N 1 # Ensure that all cores are on one machine
#SBATCH -t 3-00:00 # Runtime in D-HH:MM
#SBATCH -J fastqc
#SBATCH --output=fastqc-%A_%a.out
#SBATCH --array=1-6 # job array index
 
#SBATCH --cpus-per-task=1 # Request that ncpus be allocated per process.
 
module load FastQC/0.11.5
 
# get file name
file=`ls *_1.fastq | head -n $SLURM_ARRAY_TASK_ID | tail -n 1`
 
echo "parsing sample: "$file
 
fastqc -o ./fastqc_posttrim/ $file
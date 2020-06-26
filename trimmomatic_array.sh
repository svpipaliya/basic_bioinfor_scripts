#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --account=def-dacks
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --account=def-dacks
#SBATCH --mail-user=pipaliya@ualberta.ca

module load nixpkgs/16.09
module load trimmomatic/0.36

echo "Starting task $SLURM_ARRAY_TASK_ID"
DIR=$(sed -n "${SLURM_ARRAY_TASK_ID}p" job.conf)
cd $DIR

java -jar $EBROOTTRIMMOMATIC/trimmomatic-0.36.jar PE *_1.fastq.gz *_2.fastq.gz *_1_output_forward_paired.fq.gz *_1_output_forward_unpaired.fq.gz *_2_output_reverse_paired.fq.gz *_2_output_reverse_unpaired.fq.gz ILLUMINACLIP:NexteraPE-PE.fa:2:30:10:2:keepBothReads LEADING:3 TRAILING:3 MINLEN:36

#end
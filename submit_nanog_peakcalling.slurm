#!/bin/bash
#SBATCH --job-name=nanog_peakcalling
#SBATCH --output=nanog_peakcalling.out
#SBATCH --error=nanog_peakcalling.err
#SBATCH --time=01:00:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=2

# Load MACS3 module
module load macs

# Define paths
CHIP=~/BME110/ChIP-Seq/NanogBamFiles/NanogChIP.bam
CTRL=~/BME110/ChIP-Seq/NanogBamFiles/INPUT.bam
OUTDIR=~/BME110/ChIP-Seq/NanogPeaks

# Run MACS3
macs3 callpeak -t $CHIP -c $CTRL -f BAM -g hs -n Nanog --outdir $OUTDIR --nomodel --shift -100 --extsize 200

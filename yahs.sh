#PBS -N yahs
#PBS -P dy44
#PBS -q normalsr
#PBS -l walltime=1:00:00
#PBS -l ncpus=104
#PBS -l mem=256GB
#PBS -l jobfs=32GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44


yahs --no-contig-ec /g/data/dy44/r12.24_Themeda/themeda_noorg.fasta /g/data/dy44/r12.24_Themeda/themeda_dedup.bam
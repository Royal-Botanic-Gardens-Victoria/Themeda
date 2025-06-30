#PBS -P dy44
#PBS -N bam2fasta
#PBS -q normalsr
#PBS -l walltime=2:00:00
#PBS -l ncpus=48
#PBS -l mem=128GB
#PBS -l jobfs=64GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44

module load samtools



samtools fasta --threads 48 $PBS_O_WORKDIR/*.bam > $PBS_O_WORKDIR/reads.fasta





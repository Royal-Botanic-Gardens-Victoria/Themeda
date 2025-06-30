#PBS -N themeda-red
#PBS -P dy44
#PBS -q normal
#PBS -l walltime=4:00:00
#PBS -l ncpus=48
#PBS -l mem=190GB
#PBS -l jobfs=400GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44



infile="reads.fasta"
outfile="them-rpt.bed"

cd $PBS_JOBFS
mkdir red

#for speed using ensembl repeat mask pipeline

Red2Ensembl.py --cor 48 $infile red/

AnnotRedRepeats.py --cor 12 --bed_file $outfile /g/data/nm31/bin/plant-scripts/files/nrTEplantsJune2020.fna red/


rsync -rut $outfile $PBS_O_WORKDIR


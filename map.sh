#PBS -N them-map
#PBS -P dy44
#PBS -q normalsr
#PBS -l walltime=12:00:00
#PBS -l ncpus=48
#PBS -l mem=190GB
#PBS -l jobfs=400GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44


assembly=themeda_hic.fasta
reads=$PBS_O_WORKDIR/reads.fasta

maptype="map-hifi"

module load samtools

#cd $PBS_JOBFS #n.b. save to g/data, map files could be too large


minimap2 -t 104 -a -x $maptype $assembly $reads --secondary=no | samtools sort -m 1G -o aligned.bam -T tmp.ali

#rsync -rut * $PBS_O_WORKDIR




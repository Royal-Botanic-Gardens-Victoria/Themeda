#PBS -P dy44
#PBS -N them-hifiasm
#PBS -q normalsr
#PBS -l walltime=48:00:00
#PBS -l ncpus=104
#PBS -l mem=500GB
#PBS -l jobfs=400GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44


mkdir -p hifiasm-nohic

cd $PBS_JOBFS

#hifiasm

OUTNAME=triandra

cp $PBS_O_WORKDIR/reads.fasta ./
#cp $PBS_O_WORKDIR/*.fastq.gz ./


hifiasm --lowQ 0 -o $OUTNAME -t 104 reads.fasta #--h1 hic1_R1.fastq.gz,hic2_R1.fastq.gz --h2 hic1_R2.fastq.gz,hic2_R2.fastq.gz

awk '/^S/{print ">"$2;print $3}' $OUTNAME.bp.p_ctg.gfa > $OUTNAME'_assembly.fasta'


rsync -rut triandra* $PBS_O_WORKDIR/hifiasm-nohic/



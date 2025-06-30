#PBS -P dy44
#PBS -N them-cpblast
#PBS -q normalsr
#PBS -l walltime=2:00:00
#PBS -l ncpus=48
#PBS -l mem=190GB
#PBS -l jobfs=32GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44


cd $PBS_JOBFS

query=/g/data/dy44/r12.24_Themeda/themeda_purged.fasta
outfile="cp-purged.blast"

#blastn -query $query -db /g/data/nm31/db/mt-refseq -out $outfile -outfmt '6 qseqid sseqid pident length slen qstart qend sstart send evalue bitscore stitle' -evalue 1e-7 -subject_besthit -num_threads 48 -qcov_hsp_perc 5 -max_target_seqs 5

#rsync -rut $outfile $PBS_O_WORKDIR/

blastn -query $query -db /g/data/nm31/db/cp-refseq -out $outfile -outfmt '6 qseqid sseqid pident length slen qstart qend sstart send evalue bitscore stitle' -evalue 1e-7 -subject_besthit -num_threads 48 -qcov_hsp_perc 5 -max_target_seqs 5

rsync -rut $outfile $PBS_O_WORKDIR/


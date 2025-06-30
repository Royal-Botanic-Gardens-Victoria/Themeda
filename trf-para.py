#!/usr/bin/env python3

#Theo Allnutt 2023
#run tandem repeat finder in parallel
#r17

import sys
import os
import re
import glob
import subprocess as sp
import concurrent.futures
from Bio import SeqIO

#needs trf, trf2gff and gff2fasta in path

#alphanumeric human sort
def tokenize(filename):
	digits = re.compile(r'(\d+)')
	return tuple(int(token) if match else token for token, match in ((fragment, digits.search(fragment)) for fragment in digits.split(filename)))

def trf(i):
	
	print(i)
	name1=i.split('/')[-1]
	
	
	p0=sp.Popen(f"trf {i} 2 3 3 80 10 500 2000 -d -h",shell=True).wait()
	
	p4=sp.Popen(f"mv {outfolder}/{name1}.2.3.3.80.10.500.2000.dat {outfolder}",shell=True).wait()
	
	p1=sp.Popen(f"trf2gff -i {i}.2.3.3.80.10.500.2000.dat",shell=True).wait()
	
	#p2=sp.Popen(f"rm {oufolder+i}",shell=True).wait() #delete input contig fasta
	
	p3=sp.Popen(f"gff2fasta.py {i} {i}.2.3.3.80.10.500.2000.gff3 {i}_trf.fasta 'ID='",shell=True).wait()
	

#global
	
f=open(sys.argv[1],'r')#multifasta

outfolder=sys.argv[2]

threads =int(sys.argv[3])

if outfolder[-1]!="/":
	outfolder=outfolder+"/"
	
p5=sp.Popen(f"mkdir -p {outfolder}",shell=True).wait()

for x in SeqIO.parse(f,'fasta'):
	print("splitting fasta",x.id)
	g=open(outfolder+"/"+str(x.id).split(" ")[0]+".fasta",'w')
	SeqIO.write(x,g,'fasta')
	
filelist=glob.glob(outfolder+"*.fasta")
filelist.sort(key=tokenize)

print(filelist)

if __name__ == '__main__':
	
	executor = concurrent.futures.ProcessPoolExecutor(threads)
	futures = [executor.submit(trf, i) for i in filelist]
	concurrent.futures.wait(futures)

	#for i in filelist:
	
		#trf(i)

		
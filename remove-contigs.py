#!/usr/bin/env python3

#theo allnutt 2021
#r3.12 remove unwanted seqs by id from list


import sys
import os
import re
import glob
from Bio import SeqIO

#r11

def removeseqs(i):
	print(i)
	
	f=open(i,'r')
	
	
	for x in SeqIO.parse(f,'fasta'):
	
		id1=x.id.split(" ")[0]
		
		if id1 not in removelist:
		
			SeqIO.write(x,g,'fasta')

infile=sys.argv[1] 

g = open(sys.argv[2],'w') #outfolder

removelist=sys.argv[3].split(",")


removeseqs(infile)
		


		
#!/usr/bin/env python3

#from R02.4 concatenate tandem numpts - can be used for any tandem or overlappiing blast hits


import sys
import subprocess as sp

def concat_hits(f2):

	print("Reading bed")
	for i in f2: 
		
		k=i.rstrip("\n").split("\t")
		
		id1=k[-1]
		contig=k[contigpos]
		x=int(k[startpos])
		y=int(k[endpos])
		if x<y:
			start=x
			end=y
		else:
			start=y
			end=x
			
		
		
		if contig not in contigs.keys():
			
			k3=i.rstrip("\n").split("\t")
			k3[startpos]=start
			k3[endpos]=end
			newi="\t".join(str(p) for p in k3)+"\n"
			
			contigs[contig]=[(start,end,newi)]
			
		else:
			#check if identical
			if start==contigs[contig][-1][0] and end==contigs[contig][-1][1]:

				k2=contigs[contig][-1][2].split("\t")
				k2[-1]=k2[-1].rstrip("\n")+";"+id1+"_identical"
				
				newi="\t".join(str(p) for p in k2)+"\n"
				
				contigs[contig][-1]=(start,end,newi)
			#not identical
			else:
				if start< contigs[contig][-1][1]+overlap:#catenate
					
					newstart=contigs[contig][-1][0] #file sorted by start so cannot be less than current start
					
					if end>contigs[contig][-1][1]: #if internal numpt, use existing end
						newend=end
					else:
						newend=contigs[contig][-1][1]
					
					#weight pid by lengths
					
					
					k2=contigs[contig][-1][2].split("\t")
						
					k2[startpos]=newstart
					k2[endpos]=newend
					

					k2[-1]=k2[-1].rstrip("\n")+";"+id1
					
					newi="\t".join(str(p) for p in k2)+"\n"
					
					contigs[contig][-1]=(newstart,newend,newi)
				else:#don't catenate
					contigs[contig].append((start,end,i))


#global

infile = open(sys.argv[1],'r') #input blast
g = open(sys.argv[2],'w') #out 

overlap = int(sys.argv[3]) #allowed bp of space between hits before being merged

contigpos=int(sys.argv[4]) #blast contig column - zero numbered
startpos=int(sys.argv[5]) 
endpos=int(sys.argv[6])


contigs={}
concats={}


concat_hits(infile)


#write data
for x in contigs.keys():

	for y in contigs[x]:
	
		g.write(y[2])
		
g.close()

print("done")	
		
		
		
		
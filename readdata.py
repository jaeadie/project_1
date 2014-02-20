#!/usr/bin/python

#open the data set file.
infile='GDS4506_full.soft'
fh = open(infile)

line= fh.readline()
while line[:20] != '!dataset_table_begin':
    line=fh.readline()

header= fh.readline().strip()

#defining the title for each column in the tables.

colnames={}

index=0
for title in header.split('\t'):
    colnames[title]=index
    print '%s\t%s'%(title,index)
    index=index+1



#open our output files, one per table.
genefile=open('genes.txt', 'w')
expressionfile=open('expression.txt','w')
probefile=open('probes.txt', 'w')

#defining the columns for each table.
genefields=['Gene ID', 'Gene symbol', 'Gene title']
samples=header.split('\t')[2:int(colnames['Gene title'])]
probefields=['ID_REF','Gene ID']

#defining the function to build each row.
def buildrow(row, fields):
    newrow=[]
    for f in fields:
        newrow.append(row[int(colnames[f])])
    return "\t".join(newrow)+"\n"

#adding the data from our data set into the output files.
def build_expression(row, samples):
    exprrows=[]
    for s in samples:
        newrow=[s,]
	newrow.append(row[int(colnames['ID_REF'])])
	newrow.append(row[int(colnames[s])])
	exprrows.append("\t".join(newrow))
    return "\n".join(exprrows)+"\n"
rows=0    
#try and except to help reduce and catch bugs or errors
for line in fh.readlines():
    try:
        if line[0]=='!':
            continue
        row=line.strip().split('\t')
        genefile.write(buildrow(row, genefields))
        probefile.write(buildrow(row,probefields))
        expressionfile.write(build_expression(row, samples))	
	rows=rows+1
    except:
	pass
#close outpout files
genefile.close()
probefile.close()
expressionfile.close()
#print the number of rows that have been processed
print '%s rows processed'%rows
    

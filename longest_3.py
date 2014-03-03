# this script was used to find the 3 longest gene sequences in the NC_002695.1.fasta file

# import the biopython and SeqIO  programmes to the terminal.
from Bio import SeqIO

# open the fasta file containing the sequences and open an output file for the results.
filename = "NC_002695.1.fasta"
output_file = "longest_3.fasta"
output_handler = open(output_file, 'w')

#takes all the records in the file and puts then into a list.
records = list(SeqIO.parse(filename, 'fasta'))

#sorts the list by the length of the sequence.
records.sort(cmp = lambda x,y: cmp(len(y),len(x)))

#write the top three results, which are the longest,  into the output file that was opened earlier.
SeqIO.write(records[0:3], output_handler, 'fasta')

#close the output file.
output_handler.close()


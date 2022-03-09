"""
Basic Practice with Blast
"""
from Bio import SeqIO, SearchIO
from Bio.Blast import NCBIWWW

## read in our sequence
inputfile = 'unknown_gene.fasta'
unknowngene = SeqIO.read(inputfile, 'fasta')

## send the sequence to blast online server
## NCBIWWW(program, database, sequence)
## This can take a while
result = NCBIWWW.qblast("blastn", "nt", unknowngene.seq)
blastqresult = SearchIO.read(result, 'blast-xml')

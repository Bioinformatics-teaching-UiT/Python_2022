"""
Practice with handling sequences in BioPython
"""

from Bio.Seq import Seq # Seq is the object to deal with sequences
from Bio import SeqIO # SeqIO is module to deal with input output of sequences
from Bio.SeqUtils import six_frame_translations # Only import the function six_frame_translations from the SeqUtils module

# Difference between a string and sequence
myseq = 'ATTCGCCGAT' # this is a str
myseqobj = Seq(myseq) # this is a Seq instance, so it has a bunch of extra methods specific to Seq objects

# You can count, complement, and reverse complement the sequence
print(myseqobj.count('A'))
print(myseqobj.complement())
print(myseqobj.reverse_complement())

# Fasta file with multiple sequences, use the SeqIO parse function 
filename = 'hox_a1.fasta'
parsedobj = SeqIO.parse(filename, 'fasta')

# Unexpected behaviour of the parser
# you can do one operation on your parsed object
# and then it is erased
for item in parsedobj:
    print(item)

# you cannot subset parsed FastaIterator objects
# print(parsedobj[0])
# instead, save your records to a list
# but since we printed it out before you have to reparse it in
filename = 'hox_a1.fasta'
parsedobj = SeqIO.parse(filename, 'fasta')

parsedlist = []
for item in parsedobj:
    parsedlist.append(item)
print(parsedlist)

firstseq = parsedlist[0]
print('My first sequence is: ', firstseq.seq)
print('My first sequence ID is: ',firstseq.id)
print(firstseq.description)
print(firstseq.name)

### translate the unknown gene using biopython
unknowngenefile = 'unknown_gene.fasta'
unknowngene = SeqIO.read(unknowngenefile, 'fasta')
translatedseq = six_frame_translations(unknowngene.seq)
print(translatedseq)

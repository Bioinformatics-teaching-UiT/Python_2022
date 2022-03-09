"""
Basic Biopython Introduction
"""

from Bio.Seq import Seq
from Bio import SeqIO

## Seq object
my_seq = Seq("AGTACACTGGT")
print(my_seq)
print(my_seq.complement())
print(my_seq.reverse_complement())

## SeqRecord object
# help(SeqIO.parse)

filename = 'hox_a1.fasta'
parsed = SeqIO.parse(filename, 'fasta')
parsedlist = []

for record in parsed:
    print(record.id)
    print(record.seq)
    print(len(record))
    parsedlist.append(record)

print(parsedlist[0])


someseq = Seq('TATGAGCTGCATCGAGAACTGCGAGATCAGCGGCAGGGAGGCCACCTAA')
print(someseq.translate())

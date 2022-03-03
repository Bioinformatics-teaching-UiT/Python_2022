"""
Counting DNA Nucleotides Exercise from Rosalind
https://rosalind.info/problems/dna/

1. First in a list comprehension
2. Then in a for loop that first gets the unique chars in your sequence
"""

# input sequence
seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

# first method
# countstr saves the output in a string to print out in the format requested
countsstr = ' '.join([str(seq.count(nucl)) for nucl in 'ATCG'])
print(countsstr)

# second method
# get a set of the unique characters in seq
uniq_chars = set(seq)
print(uniq_chars)

# save the counts for each unique character in a dictionary
countsdict = {}
for nucl in uniq_chars:
    countsdict[nucl] = seq.count(nucl)

# print out the result in the ATCG order
print(countsdict)
countslist = [countsdict['A'], countsdict['T'], countsdict['C'], countsdict['G']]

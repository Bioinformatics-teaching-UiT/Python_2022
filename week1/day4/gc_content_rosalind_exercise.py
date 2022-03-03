"""
gc_content_rosalind_exercise.py

Script to solve the 'Computing GC Content' exercise:
https://rosalind.info/problems/gc/

Includes
1. fasta parser to parse fasta file to form {header:seq}
2. gc percentage function
3. wrapper for gc percentage function that stores gc percents in a dictionary
4. functions to get key of max value in a dictionary
5. line-by-line procedure to tie these functions together
"""

# function to parse fasta file into fasta dictionary
def fasta_parser(fastafile):
    fa_file = open(fastafile, 'r')
    lines = fa_file.readlines()
    fa_file.close()

    fa_dict = {}
    for line in lines:
        line = line.strip()
        if line[0] == '>':
            header = line[1:]
            fa_dict[header] = ''
        else:
            fa_dict[header] += line

    return fa_dict

# function to calculate GC content given a string
def calc_GC_from_seq(someseq):
    seqlen = len(someseq)
    G_count = someseq.count('G')
    C_count = someseq.count('C')
    return 100 * (G_count + C_count) / seqlen

# function to make a GC content dictionary
# fastadict = { 'Rosalind_6404':'CCTG...',...}
# GC_dict = { 'Rosalind_6404': 23.45, ...}

def get_GC_dict(fastadict):
    GC_dict = {}
    for key in fastadict.keys():
        GC_dict[key] = calc_GC_from_seq(fastadict[key])
    return GC_dict

# function to return key, value of max value in dictionary
def get_key_of_max_val(somedict):
    maxval = 0
    maxkey = ''
    for key, val in somedict.items():
        if val > maxval:
            maxkey = key
            maxval = val
    return maxkey, maxval

# a shorter way to write this
def get_maxkey_shorter(somedict):
    maxkey = max(somedict, key=somedict.get)
    return maxkey

# try it out
filename = 'gcseqs.fasta'
fasta_dict = fasta_parser(filename)
GC_dict = get_GC_dict(fasta_dict)
# using first max key function
key_of_maxGC, val_of_maxGC = get_key_of_max_val(GC_dict)
print(f'{key_of_maxGC}\n{val_of_maxGC}')
# using second max key function
key_of_maxGC= get_maxkey_shorter(GC_dict)
print(f'{key_of_maxGC}\n{GC_dict[key_of_maxGC]}')


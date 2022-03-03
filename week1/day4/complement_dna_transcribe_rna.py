"""
This script finds the reverse complement and transcribes
your DNA sequence into RNA. It does it in two ways,
a long format with a proper for loop, then in a list comprehension.

1. First reverse complement your DNA strand
2. Then transcribe it into RNA
"""

def rev_comp_long(someseq):
    """
    Finds reverse complement of a DNA seq
    with classic for loop structure
    :param someseq: str
    :return: str
    """
    seqflipped = someseq[::-1]
    compseqlist = []
    compdict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    for nucl in seqflipped:
        if nucl in compdict.keys():
            compseqlist.append(compdict[nucl])
    return ''.join(compseqlist)


compdict = {'A':'U', 'T':'A', 'C':'G', 'G':'C'}
def rev_comp_trans(someseq, keydict):
    """
    Please do not code like this:
    Finds reverse complement of a DNA seq
    with a list comprehension
    :param someseq: str
    :return: str
    [ expression for i in range.. <if condition> ]
    [ a if a else bla for a in blabla ]
    """
    return ''.join([keydict[nucl] if nucl in keydict.keys() else 'N' for nucl in someseq[::-1]])

print(rev_comp_trans('AAAACCCGGTX', compdict))
print(rev_comp_long('AAAACCCGGT'))
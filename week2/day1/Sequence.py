"""
This script creates the class Sequence,
which will have the following characteristics.

Attributes:
    seq
    type
    ID

Methods:
    get_length
    reverse_complement

So we want to make an instance of our class as:
seq1 = Sequence('ATCCGGTA', 'dna', 'P3645G')
seq1.sequence
seq1.get_length()
seq1.reverse_complement()
"""

class Sequence:
    ## init function initialises class instance
    ## based on attributes
    def __init__(self, sequence, seqtype, ID):
        self.sequence = sequence
        self.seqtype = seqtype
        self.ID = ID

    def get_length(self):
        """
        Method to find length of your sequence
        :return: int
        """
        return len(self.sequence)

    def rev_comp(self):
        """
        Reverses the sequence and returns the complement
        :return: str
        """
        seq_reversed = self.sequence[::-1]
        compdict = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
        revcomplist = []
        for nucl in seq_reversed:
            if nucl in compdict.keys():
                revcomplist.append(compdict[nucl])
        return ''.join(revcomplist)


# create an instance of the class called seq1
seq1 = Sequence('ATCCGGTA', 'dna', 'P3645G')
print(seq1.sequence)
print(seq1.seqtype)
print(seq1.ID)
print(seq1.get_length())
print(seq1.rev_comp())

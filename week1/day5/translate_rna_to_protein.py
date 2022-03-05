"""
Script to translate RNA sequence to protein sequence
This corresponds to Rosalind exercise:
https://rosalind.info/problems/prot/
1. parse rna codon table
2. translate to protein sequence
"""

def parse_codon_table(filename):
    """
    Reads in a codon table and parses
    it into dictionary form {codon:amino acid}
    :param filename: str
    :return: dict
    """
    f = open(filename,'r')
    lines = f.readlines()
    f.close()

    codon_to_aa_dict = {}
    all_pairs_list = []
    for line in lines:
        pairslist = line.strip().split()
        all_pairs_list.extend(pairslist)
    for i, elem in enumerate(all_pairs_list):
        if i % 2 == 0:
            codon_to_aa_dict[elem] = all_pairs_list[i+1]
    return codon_to_aa_dict


def translate_rna_prot(rna_seq, translation_dict):
    """
    Translates rna sequence to protein sequence
    based on rna triplet code
    :param rna_seq: str
    :param translation_dict: dict
    :return: str
    """
    translated_seq = ''
    for i in range(0, len(rna_seq), 3):
        translated_seq += translation_dict[rna_seq[i:i+3]]
    return translated_seq

rosalind_seq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
print(translate_rna_prot(rosalind_seq, parse_codon_table('rna_codon_table.txt')))


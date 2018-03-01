def to_rna(dna_strand):
    table = {'A': 'U',
           'C': 'G',
           'G': 'C',
           'T': 'A'}
    return ''.join([table[c] for c in dna_strand])

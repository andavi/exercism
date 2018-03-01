def to_rna(dna_strand):
    map = {'A': 'U',
           'C': 'G',
           'G': 'C',
           'T': 'A'}
    return ''.join([map[c] for c in dna_strand])

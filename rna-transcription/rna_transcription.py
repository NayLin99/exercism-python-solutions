def to_rna(dna_strand):
    dna_to_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna = ""
    for char in dna_strand:
        rna += dna_to_rna.get(char)
    return rna

def proteins(strand):
    split_string = [strand[i : i + 3] for i in range(0, len(strand), 3)]
    protein_str = []

    for i in split_string:
        if i == "UAA" or i == "UAG" or i == "UGA":
            break
        elif i == "AUG":
            protein_str.append("Methionine")
        elif i == "UUU" or i == "UUC":
            protein_str.append("Phenylalanine")
        elif i == "UUA" or i == "UUG":
            protein_str.append("Leucine")
        elif i == "UCU" or i == "UCC" or i == "UCA" or i == "UCG":
            protein_str.append("Serine")
        elif i == "UAU" or i == "UAC":
            protein_str.append("Tyrosine")
        elif i == "UGU" or i == "UGC":
            protein_str.append("Cysteine")
        elif i == "UGG":
            protein_str.append("Tryptophan")

    return protein_str

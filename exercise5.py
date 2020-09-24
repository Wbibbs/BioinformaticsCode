dna = 'ATTTGAATAGCCCGAGCAGCAGGACGAGTTAGTAGCTATCCCGTATTGTTAGGTA'
dna = dna[0:len(dna):1]
GC_count = dna.count('G') + dna.count('C')
print('GC Percentage: ' + str((GC_count * 100.0 / len(dna))))

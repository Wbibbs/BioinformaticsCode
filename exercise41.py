# get DNA sequence
dna="acgctcgcgcgcggcgatagctgatcgatcggccgcgcgttttttttaaaag"
#get the number of c's in the sequence and store it in the variable no_c
no_c=dna.count("c")
#get the number of g's in the sequence and store it in the variable no_g
no_g=dna.count("g")
#store the length of the DNA sequence in the variable dna_length
dna_length=len(dna)
#compute the gc percentage and store it in the variable gc_percent
gc_percent=(no_c+no_g)*100/dna_length
#print the value of the gc percentage
print(gc_percent)

#Get dna
dna= "atgggccccaaagggggggccccttttaaaaggggccccaaattt"

#get the number of t's in the sequence and store it in the variable no_c
no_a=dna.count("a")
#get the number of a's in the sequence and store it in the variable no_g
no_t=dna.count("t")
#store the length of the DNA sequence in the variable dna_length
dna_length=len(dna)
#compute the gc percentage and store it in the variable gc_percent
at_percent=(no_a+no_t)*100/dna_length
#print the value of the gc percentage
print(at_percent)
print('Total: ' + str(at_percent + gc_percent))

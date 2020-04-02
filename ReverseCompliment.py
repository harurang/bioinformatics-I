nucleotide = 'AAAACCCGGT'

def getReverseCompliment():
  complementaryNucleotide = ''
  for i in range(0, len(nucleotide)):
    print(nucleotide[i])
    if (nucleotide[i] == 'C'):
      complementaryNucleotide += 'G'
    if (nucleotide[i] == 'G'):
      complementaryNucleotide += 'C'
    if (nucleotide[i] == 'A'):
      complementaryNucleotide += 'T'
    if (nucleotide[i] == 'T'):
      complementaryNucleotide += 'A'

  return ''.join(reversed(complementaryNucleotide));

print(getReverseCompliment())

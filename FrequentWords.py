# Input: A string Text and an integer k.
# Output: All most frequent k-mers in Text.

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4 # length we want our k-mers to be

# Given and index and a charcter determine if that index is the beginning of a kmer with lenght k.
# If it is, get the kmer and return it.
def getKmerIfExists(index, charc):
  possibleKmer = text[index]
  for i in range(index + 1, len(text)):
    pattern = possibleKmer + text[i]
    if len(pattern) < k and text.count(pattern) > 1:
      possibleKmer += text[i]
    elif len(pattern) == k:
      return pattern
    else:
      break

# For each character of text, check if it is a kmer.
# Return list of kmers.
def getKMers():
  kmers = []
  for i in range(0, len(text)):
    kmer = getKmerIfExists(i, text[i])
    if (kmer):
      kmers.append(kmer)
  return kmers

# For all kmers, find the most frequent and return them.
def getMostFrequentKmers():
  kmers = getKMers()
  mostFrequentKmers = []
  highestCount = 0
  for i in range(0, len(kmers)):
    if (text.count(kmers[i]) >= highestCount):
      highestCount = text.count(kmers[i])
      # If there are kmers and the first kmer has a lower count than highest count,
      # replace it
      if (len(mostFrequentKmers) and text.count(mostFrequentKmers[0]) < highestCount):
        mostFrequentKmers = [kmers[i]]
      elif kmers[i] not in mostFrequentKmers:
        mostFrequentKmers.append(kmers[i])
  return mostFrequentKmers

print(getMostFrequentKmers())

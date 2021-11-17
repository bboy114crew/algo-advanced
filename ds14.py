# Knuth-Morris-Pratt

def KMP_preprocess(P, prefix):
  prefix[0] = 0
  i = 1
  j = 0
  m = len(P)
  while i < m:
    if P[i] == P[j]:
      j += 1
      prefix[i] = j
      i += 1
    else:
      if j != 0:
        j = prefix[j - 1]
      else:
        prefix[i] = 0
        i += 1

P = 'AAACAAAAACC'

prefix = [0 for _ in range(len(P))]

KMP_preprocess(P, prefix)

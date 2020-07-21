# Escreva dois algoritmos distintos de ordenacao de sequencia. Em seguida mostre
# o passo a passo para a  sequencia L = {2, 7, 5, 6, 9, 0, 1, 4,  8, 5, 3}

l = [2, 7, 5, 6, 9, 0, 1, 4,  8, 5, 3]


def algoritmo1(s):

  
  for i in range( 0, len(s) - 1):

    k = i

    while k >= 0 and s[k] > s[k+1]:
      s[k], s[k+1] = s[k+1], s[k]
      k -= 1
      print(s)

   

    
#algoritmo1(l)
#print(l)



def algoritmo2(s):
  ''' QuickSort '''
  if s:
    left = [x for x in s if x < s[0]]
    right = [x for x in s if x > s[0]]
    print(left + [s[0]]  * s.count(s[0]) + right)
    return algoritmo2(left) + [s[0]] * s.count(s[0]) + algoritmo2(right)
  return []

#algoritmo1(l)
print(algoritmo2(l))

print(l)
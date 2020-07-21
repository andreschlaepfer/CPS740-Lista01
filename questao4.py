graph1 = {
  'a' : ['b', 'd'],
  'b': ['a', 'e'],
  'c': ['b', 'd'],
  'd': ['a', 'c'],
  'e': ['b', 'd']
}

graph2 = {
  'a' : ['b', 'd'],
  'b': ['a', 'e'],
  'c': ['b', 'd'],
  'd': ['a', 'c', 'b'],
  'e': ['b', 'd']
}

def isBipartite(graph):

  arb_v = list(graph.keys())[0]

  v1 = [arb_v]
  v2 = []

  for i in graph[arb_v]:

    for j in graph[i]:
      if j != arb_v:
        v1 += [j]

  for i in v1:
    for j in graph[i]:
      for  x in j:
        if x in v1:
          return False

  return True
#print(graph1[0])

print(isBipartite(graph1))

#print(graph1[list(graph1.keys())[0]])
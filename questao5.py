
graph1 = {
  'a' : ['b', 'd'],
  'b': ['a', 'e'],
  'c': ['b', 'd'],
  'd': ['a', 'c'],
  'e': ['b', 'd']
}


def hasIndependentSizeK(graph, k):

 

  v1 = []
  v2 = []

  for i in graph:

    for j in graph[i]:
      if j != i:
        v1 += [j]

    for i in graph:
      if i not in v1:
        v2 += [i]
    
    if len(v1) or len(v2) == k:
      return True

  return False



def hamilton(graph, size, pt, path=[]):
    
  
  if pt not in set(path):
      path.append(pt)
      if len(path)==size:
          return True
      for pt_next in graph.get(pt, []):
          res_path = [i for i in path]
          candidate = hamilton(graph, size, pt_next, res_path)
          if candidate is not None:  
              return candidate
      return False
  
    


print(hamilton(graph2, 5, 'a'))
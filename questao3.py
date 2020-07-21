
graph1 = {
  'a' : ['b', 'e'],
  'b' : ['a', 'c', 'd', 'f'],
  'c' : ['b', 'f', 'd', 'e'],
  'd' : ['b', 'c','e', 'f'],
  'e' : ['a', 'c', 'd', 'f'],
  'f' : ['b', 'c', 'd', 'e']
}

graph2 = {
  'a' : ['b', 'e'],
  'b' : ['a', 'c', 'd', 'f'],
  'c' : ['b', 'f', 'd', 'e'],
  'd' : ['b', 'c','e', 'f'],
  'e' : ['a', 'c', 'd', 'f'],
  'f' : ['a','b', 'c', 'd', 'e']
}


def isEulerian(graph):
  for i in graph:
    if len(graph[i])%2 != 0:
      return False
  return True


print(isEulerian(graph1))
print(isEulerian(graph2))


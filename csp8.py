def colour_vertices(graph):


  vertices = sorted((list(graph.keys())))
  colour_graph = {}

  for vertex in vertices:
    unused_colours = len(vertices) * [True]

    for neighbor in graph[vertex]:
      if neighbor in colour_graph:
        colour = colour_graph[neighbor]
        unused_colours[colour] = False
    for colour, unused in enumerate(unused_colours):
      if unused:
        colour_graph[vertex] = colour
        break

  return colour_graph




graph = { "a" : ["c", "d", "b"],
          "b" : ["c", "e", "a"],
          "c" : ["a", "b"],
          "d" : ["a","e"],
          "e" : ["d", "b"],
         }
result = (colour_vertices(graph))
print(result)

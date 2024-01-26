def depth_limited_search(node, goal, depth_limit, visited=set()):
     if node == goal:
        return [node]
     elif depth_limit == 0:
        return None
     else:
        visited.add(node)
        for child in get_children(node):
           if child not in visited:
              path = depth_limited_search(child, goal, depth_limit - 1, visited.copy())
              if path is not None:
                 return [node] + path
              return None
def get_children(node):
     adjacency_list = { 'A':['B','C'],'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': [] }
     return adjacency_list.get(node, [])
result = depth_limited_search('A','D',2 )
if result is not None:
    print("Path found:", result)
else:
    print("No path found within depth limit")

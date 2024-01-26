from collections import defaultdict
visited = defaultdict(lambda : False)
jug1 = int(input(&quot;Enter the max capacity of jug 1: &quot;))
jug2 = int(input(&quot;Enter the max capacity of jug 2: &quot;))
aim = int(input(&quot;Enter the capacity needed: &quot;))
def waterJugSolver(amt1, amt2):
if((amt1==0 and amt2==aim) or (amt1==aim and amt2==0)):
print(amt1,amt2)
return True
if(visited[(amt1, amt2)]) == False:
print(amt1, amt2)
visited[amt1, amt2] = True
return (waterJugSolver(0, amt2) or waterJugSolver(amt1,0) or waterJugSolver(jug1,
amt2) or waterJugSolver(amt1, jug2) or waterJugSolver(amt1+min(amt2, jug1-amt1), amt2 - min(amt2,
jug1-amt1)) or waterJugSolver(amt1-min(amt1, jug2-amt2), amt2 + min(amt2, jug2-amt2)))
else:
return False

print(&#39;Steps: &#39;)
print(waterJugSolver(0,0))

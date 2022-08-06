from collections import defaultdict

class Node():
	def __init__(self, val):
		self.disc = 0
		self.low = 0
		self.parent = None
		self.childCount = 0
		self.visited = False
		self.val = val

def findArticulationPoint(edges):
	graph = defaultdict(list)
	time = 0
	articulationPoints = set()

	def dfs(u: Node):
		nonlocal time
		u.disc = time
		u.low = time
		time +=1
		u.visited = True

		for v in graph[u]:
			if not v.visited:
				u.childCount +=1
				v.parent = u
				
				dfs(v)

				u.low = min(u.low, v.low)

				if u.parent == None and u.childCount >1:
					articulationPoints.add(u.val)
				if u.parent != None and v.low >= u.disc:
					articulationPoints.add(u.val)
			elif v != u.parent:
				u.low = min(u.low, v.disc)

	val_vs_node = {}
	for u,v in edges:
		u_node = val_vs_node.get(u)
		if u_node == None:
			u_node = Node(u)
			val_vs_node[u] = u_node
		v_node = val_vs_node.get(v)
		if v_node == None:
			v_node = Node(v)
			val_vs_node[v] = v_node
		graph[u_node].append(v_node)
		graph[v_node].append(u_node)

	dfs(val_vs_node[0])
	print(articulationPoints)

findArticulationPoint([(0,1),(0,2),(1,2),(1,3),(1,4),(2,3)])
	

from vertex import Vertex

class Graph(object):
	
	def __init__(self, graph, v, e):
		if graph == None:
			graph = {}

		self.graph_dict = graph
		self.disc_list = []
		self.adj_mtx = []
		self.v = v
		self.e = e
		self.adj_lst = [[] for x in range(self.v)]
		self.index = 0
		self.stack = []
		self.VList = []
		self.EList = []
		self.visited = {}
		self.parent = [[] for x in range(self.v)]
		self.sortNodes = []
		self.nodeTemp = 0

		for x in range(self.v):
			self.visited[x+1] = False

		
	def vertices(self):
		return list(self.graph_dict.keys())

	def add_vertex(self, num):
		vObj = Vertex(num)
		flag = True
		for x in self.VList:
			if vObj.num == x.num:
				flag = False
				break

		if flag:
			self.VList.append(vObj)

		if num not in self.graph_dict:
			self.graph_dict[num] = []

	def edges(self):
		edge_list = []

		for x in self.graph_dict:
			for y in self.graph_dict[x]:
				if {x,y} not in edge_list:
					edge_list.append(str(x)+","+str(y))

		return edge_list

	def adj_matrix(self):
		some = [[0 for x in range(1,self.v+1)] for x in range(1,self.v+1)]
		for x in self.graph_dict:
			for y in self.graph_dict[x]:
				some[x-1][y-1] = 1
		
		self.adj_mtx = some

		return self.adj_mtx

	def add_edge(self, edge):
		num = int(edge.split(",")[0])
		num2 = int(edge.split(",")[1])
		
		v1 = Vertex(num)
		v2 = Vertex(num2)

		self.add_vertex(num)
		self.add_vertex(num2)
		
		self.graph_dict[num].append(num2)
		self.EList.append((v1,v2))

	
	def adj_list(self):
		for x in self.graph_dict:
			self.adj_lst[x-1] = self.graph_dict[x]

		return self.adj_lst

	"""
	def tarjanStart(self):
		
		for v in self.VList:
			if v.index == -1:
				self.strongConnect(v)


	def strongConnect(self, v):
		v.index = self.index
		v.lowLink = self.index
		self.index += 1

		self.stack.append(v)
		v.onStack = True

		for (v,w) in self.EList:
			if w.index == -1:
				self.strongConnect(w)
				v.lowLink = min(v.lowLink, w.lowLink)
			elif w.onStack:
				v.lowLink = min(v.lowLink, w.index)

		if v.lowLink == v.index:
			strng = []
			
			w = Vertex(None)
			while w.num != v.num:
				if len(self.stack) > 0:
					w = self.stack.pop()
					w.onStack = False
					strng.append(w)
				else:
					break

			for x in strng:
				print x,
			if len(strng) > 0:
				print ""
	"""

	def dfs(self,node1, node2):
		if self.visited[node2]:
			if(node1 == node2):
				self.count += 1
				for x in range(len(self.parent)):
					self.parent[x] = list(set(self.parent[x]))

				self.nodeTemp = node2

				print self.parent
			return

		self.visited[node2] = True

		for x in self.adj_lst[node2-1]:
			self.parent[x-1].append(node2)
			self.dfs(node1, x)

		self.visited[node2] = False

	def allCycles(self):
		self.count = 0
		for x in self.VList:
			self.dfs(x.num, x.num)
			self.visited[x.num] = True


	def topSort(self):
		for x in self.VList:
			if not x.permMark:
				self.visit(x)

	def visit(self, node):
		if node.tempMark:
			return

		if not node.permMark:
			node.tempMark = True
			
			for (node, node2) in ( x for x in self.EList if x[0] == node ):
				self.visit(node2)

			node.permMark = True
			node.tempMark = False

			self.sortNodes.append(node.num)




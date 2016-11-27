class Vertex(object):
	
	def __init__(self, num):
		self.index = -1
		self.lowLink = -1
		self.onStack = False
		self.tempMark = False
		self.permMark = False
		self.num = num

	def __str__(self):
		return str(self.num)

	
import openpyxl as ex
from graph import Graph

wb = ex.load_workbook(filename = 'Dataset2.xlsx')
sheet = wb['Sheet1']
data=[]

for row in sheet.iter_rows():
    for k in row:
        data.append(k.internal_value)

v = int(str(data[0]).split("=")[1].strip())
e = int(str(data[1]).split("=")[1].strip())

edge_cor = []
graph1 = Graph({},v,e)

for x in range(2, (e+1)*2, 2):
	st = str(data[x])
	en = str(data[x+1])

	graph1.add_edge(st+","+en)

"""
for x in graph1.adj_matrix():
	for y in x:
		print y,
	print ""
"""

graph1.adj_list()

graph1.allCycles()

if graph1.count == 0:
	graph1.topSort()
	print "Topological Order"
	print graph1.sortNodes

import openpyxl as ex

wb = ex.load_workbook(filename = 'Dataset4.xlsx')
sheet = wb['Sheet1']
data=[]

for row in sheet.iter_rows():
    for k in row:
        data.append(k.internal_value)

v = int(str(data[0]).split("=")[1].strip())
e = int(str(data[1]).split("=")[1].strip())

edge_cor = [[0 for x in range(1,v+1)] for x in range(1,v+1)]

for x in range(2, (e+1)*2, 2):
	#print x
	st = int(data[x]-1)
	en = int(data[x+1]-1)

	edge_cor[st][en] = 1

print "Adjacency matrix: "
for x in edge_cor:
	for y in x:
		print y,
	print ""

def readFile(file):
	namesList = list()
	outputList = list()
	with open(file) as f:
		f.readline()
		for i in f:
			count = int(i)
			for j in range(count):
				namesList.append(f.readline().replace('\n',''))
			leader = findLeader(namesList)
			namesList.clear()
			outputList.append(leader[0])
	return outputList	

def formatOutput(outputList):
	f = open("b.out", 'w')
	for c, i in enumerate(outputList): 
		output = "Case #{}: {}\n".format(c+1, i)
		print(output)
		f.write(output)

def main():
	readFile('b.in')
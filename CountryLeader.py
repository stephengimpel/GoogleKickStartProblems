#Reads each line of the file and stores it in a list
def readFile(file):
	fullList = list()
	with open(file) as f:
		f.readline()
		numberOfNames = int(f.readline())
		for i in range(numberOfNames):
			fullList.append(i)
	return fullList

def findLeader(namesList):
	


def main():
	print("stub")

main()
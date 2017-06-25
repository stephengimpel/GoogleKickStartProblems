import string

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
	

def countDistinctLetters(names):
	alaphabet[26] = 0
	count = 0
	size = len(names)
	for i in range(size):
		letterIndex = alphabet[string.lowercase.index(names[i])]
		if letterIndex == 0:
			count += 1
			letterIndex = 1
	return count

def main():
	print("stub")

main()

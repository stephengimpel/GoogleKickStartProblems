import string
#Reads each line of the file and stores it in a list
def readFile(file):
	namesList = list()
	with open(file) as f:
		f.readline()
		numberOfNames = int(f.readline())
		for i in range(numberOfNames):
			namesList.append(f.readline().replace('\n',''))
		leader = findLeader(namesList)
		print(leader)

def findLeader(namesList):
	currentLeader = list()
	currentLeader.append(namesList.pop())
	for i in namesList:
		if(countDistinctLetters(currentLeader[0]) < countDistinctLetters(i)):
			currentLeader.clear()
			currentLeader.append(i)
		elif(countDistinctLetters(currentLeader[0]) == countDistinctLetters(i)):
			currentLeader.append(i) 

	return currentLeader


def countDistinctLetters(names):
	alphabet[26] = 0
	count = 0
	size = len(names)
	for i in range(size):
		letterIndex = alphabet[string.lowercase.index(names[i])]
		if letterIndex == 0:
			count += 1
			letterIndex = 1
	return count

def main():
	readFile('temp.in')

main()

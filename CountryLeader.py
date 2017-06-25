#Reads each line of the file and stores it in a list
def readFile(file):
	namesList = list()
	with open(file) as f:
		f.readline()
		for i in f:
			count = int(i)
			for j in range(count):
				namesList.append(f.readline().replace('\n',''))
			leader = findLeader(namesList)
			namesList.clear()
			print(leader)	


def findLeader(namesList):
	currentLeader = list()
	currentLeader.append(namesList.pop())
	for i in namesList:
		if(countDistinct(currentLeader[0]) < countDistinct(i)):
			currentLeader.clear()
			currentLeader.append(i)
		elif(countDistinct(currentLeader[0]) == countDistinct(i)):
			currentLeader.append(i) 

	return currentLeader


def countDistinctLetters(names):
	alphabet = list()
	for i in range(26):
		alphabet.append(False)
	count = 0
	for i in names:
		letterIndex = alphabet[string.ascii_uppercase.index(i)]
		if letterIndex == False:
			count += 1
			letterIndex = True
	return count


def countDistinct(name):
	unique = list()
	count = 0
	for i in name:
		if(not i in unique):
			unique.append(i)
			count += 1

	return count

def main():
	namesList = readFile('temp.in')
	

main()

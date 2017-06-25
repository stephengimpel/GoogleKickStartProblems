import string
#Reads each line of the file and stores it in a list
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

def findLeader(namesList):
	currentLeader = list()
	currentLeader.append(namesList.pop())
	for i in namesList:
		if(countDistinctLetters(currentLeader[0]) < countDistinctLetters(i)):
			currentLeader.clear()
			currentLeader.append(i)
		elif(countDistinctLetters(currentLeader[0]) == countDistinctLetters(i)):
			currentLeader.append(i) 
	currentLeader.sort()
	return currentLeader

def formatOutput(leaders):
	f = open("CountryLeader.out", 'w')
	for c, i in enumerate(leaders): 
		output = "Case #{}: {}\n".format(c+1, i)
		print(output)
		f.write(output)

#Davids "Blazing memory efficent C liek" function
def countDistinctLetters(names):
    alphabet = [False for x in range(26)]
    count = 0
    size = len(names)
    for i in range(size):
        if names[i] == " ":
            continue
        letterIndex = string.ascii_uppercase.index(names[i])
        if alphabet[letterIndex] == False:
                count += 1
                alphabet[letterIndex] = True
    return count

#Stephens "super duper readable" function
def countDistinct(name):
	unique = list()
	count = 0
	for i in name:
		if(not i in unique):
			unique.append(i)
			count += 1

	return count

def main():
	output = readFile('CountryLeaderLarge.in')
	formatOutput(output)

main()

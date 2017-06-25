import math

def readFile(file):
	ij = list()
	pattern = list()
	with open(file) as f:
		f.readline()
		count = 0
		for i in f:
			if(count % 2 == 0):
				i = i.replace("\n", "")
				pattern.append(i)
			else:
				i = i.replace("\n", "")
				i = i.split(" ")
				ij.append(i)
			count +=1
			
	return ij, pattern

def countBlue(end, pattern):
	blues = 0
	#print("start: {} \t end: {} \t pattern: {}".format(start, end, pattern))
	for i in range(len(pattern)):
		if(pattern[i] == 'B'):
			blues += 1
	whole = math.floor(end / len(pattern))
	remaining = end % len(pattern)
	blues += whole * blues
	for i in range(remaining):
		if(pattern[i] == 'B'):
			blues += 1
	return blues


def iterateData(ij, pattern):
	f = open("answer.txt", "w")
	for c, i in enumerate(pattern):
		totalBlues = countBlue(int(ij[c][1]), i)
		totalBlues -= countBlue(int(ij[c][0])-1, i)
		string = "Case #{}: {}\n".format(c+1, totalBlues)
		f.write(string)
		print(string)

def main():
	ij, pattern = readFile("lights.in")
	iterateData(ij, pattern)
	
main()
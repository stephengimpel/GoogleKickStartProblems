import math

#Reads each line of the file and stores it in a list
def readFile(file):
	cordList = list()
	with open(file) as f:
		f.readline()
		for i in f:
			cordList.append(i)
	return cordList

#Scrapes off useless white space and \n, stores cordinates in 2d array
def prepList(cordinates):
	cordList = list()
	for i in cordinates:
		i = i.replace("\n", "")
		temp = i.split(" ")
		cordList.append(temp)
	return cordList

def toSmallerSquares(row, column, squares):
	#print("rows: {} \t columns: {}".format(row, column))
	if(row < 2 or column < 2):
		return 0 
	elif(row == 2 and not column < 2):	#smallest cases are 2 rows or columns. Then multiple out
		return column
	elif(not row < 2 and column == 2):
		return row
	# elif(row == 3 and not column < 2):
	# 	return 2 * column
	# elif(not row < 2 and column == 3):
	# 	return 2 * row
	else:
		squares += toSmallerSquares(math.floor(row/2), math.floor(column/2), squares)
		squares += toSmallerSquares(math.ceil(row/2), math.floor(column/2), squares)
		squares += toSmallerSquares(math.floor(row/2), math.ceil(column/2), squares)
		squares += toSmallerSquares(math.ceil(row/2), math.ceil(column/2), squares)

	return squares

#Start of application
def main():
	cordList = prepList(readFile("smaller-test.in"))
	for i in cordList:
		print(i)
		answer = toSmallerSquares(int(i[0]), int(i[1]), 0)
		print(answer)


main()
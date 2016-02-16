f = open("8ptext.txt","r")

print "\nThe initial array:"
fileLines = []

lines = 0
for line in f:
	if(line!="\n"):
		lines+=1
		if(lines>8):
			break
		print line[:8]
		fileLines.append(line[:8])
print fileLines

# fileLines format = ['12345678','12345678','12345678','12345678','12345678','12345678','12345678','12345678']
# When left rotating we have to print, starting from the last character 
# of each list item.
def rotateLeft():
	global fileLines 
	lst = []
	print "\nLeft rotation." 
	for i in range(7,-1,-1):
		string = ''
		for j in range(8):
			string += fileLines[j][i]
		lst.append(string)
		print string	
	fileLines = lst
# When right rotating we have to print, starting from the first character 
# of each list item.	
def rotateRight():
	global fileLines
	lst = []
	print "\nRight rotation."
	for i in range(8):
		string = ''
		for j in range(7,-1,-1):
			string += fileLines[j][i]
		lst.append(string)
		print string
	fileLines = lst



print "\nEnter \"r\" for right rotation,"
print "Or \"l\" for left rotation."
print "Press \"q\" to Exit."
move = raw_input()
while(move!="q"):
	if(move == "r"):
		rotateRight()
	elif(move == "l"):
		rotateLeft()
	move = raw_input()
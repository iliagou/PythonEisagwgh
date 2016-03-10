f = open('pinakas.txt')
d = f.readlines()
d = [x.split() for x in d]
print "-----------arxikos pinakas------------"
print ('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in d]))
f.close()
print "--------------------------------------"
for i in range (3) :
	d = list(reversed(zip(*d)))
	print ('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in d]))
	print "--------------------------------------"

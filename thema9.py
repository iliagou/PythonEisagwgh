from random import randint

flag = True

A = [[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],]

# counters for A's columns
K = [19,19,19,19,19,19,19,19,19,19]




# Helper function for print2dList.
# This finds the maximum length of the string
# representation of any item in the 2d list
def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in xrange(rows):
        for col in xrange(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen

# prints 2d lists a bit nicer.
def print2dList(a):
    if (a == []):
        # So we don't crash accessing a[0]
        print []
        return
    rows = len(a)
    cols = len(a[0])
    fieldWidth = maxItemLength(a)
    #print "[ ",
    for row in xrange(rows):
        if (row > 0): print "\n",
        print "",
        for col in xrange(cols):
            if (col > 0): print " ",
            # The next 2 lines print a[row][col] with the given fieldWidth
            format = "%" + str(fieldWidth) + "s"
            print format % str(a[row][col]),
        #print "]",
    print " "




# add in j column
def add(b,j):
	A[b][j] = "|"

# add in j+1 column
def add2(v,j):
	A[v][j] = "_"


# L counter
countL = 0


while (flag):

	# random column
	j = randint(0,8)
	j2 = j + 1

# if gia to pou tha kathisei to L. eite sto j eite sto j+1
	# kathete sto j
	if (K[j] < K[j2]):
		K[j2] = K[j]
		if (K[j]<2) or (K[j2]<2):
			flag = False
		else:	
			for a in range(3):
				add(K[j],j)
				K[j] -=1
			add2(K[j2],j2)
			K[j2] -=1
			countL += 1
	# kathete sto j+1
	elif (K[j] > K[j2]):
		K[j] = K[j2]
		if (K[j]<2) or (K[j2]<2):
			flag = False
		else:	
			for a in range(3):
				add(K[j],j)
				K[j] -=1
			add2(K[j2],j2)
			K[j2] -=1
			countL += 1
	# kathete kai sta 2 mazi
	else:
			if (K[j]<2) or (K[j2]<2):
				flag = False
			else:	
				for a in range(3):
					add(K[j],j)
					K[j] -=1
				add2(K[j2],j2)
				K[j2] -=1
				countL += 1


	
	if (K[j] < 2) or (K[j2] < 2):
		flag = False



print countL
print2dList(A)
#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))



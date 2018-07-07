i=0
numbers=[]

while i<6:
    print "At the top i is %d" % i
    numbers.append(i)
    i=i+1

for i in numbers:
    print i

numbers=[]

for i in range(0,6):
    print "Append %d" % i
    numbers.append(i)

for i in numbers:
    print i

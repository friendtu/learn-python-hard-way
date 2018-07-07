ten_things = "Apples Oranges Crows Telephone Light Sugar"
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

stuff=ten_things.split(' ')
while len(stuff)<10:
    one=more_stuff.pop()

    print "add %s." % one
    stuff.append(one)

print "There are %d item in stuff" % len(stuff)

print "stuff[1] is %s." % stuff[1]
print "stuff[-1] is %s." % stuff[-1]

print " ".join(stuff)
print "#".join(stuff[3:5])
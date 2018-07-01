def print_two(*args):
  arg1,arg2=args
   print "arg1: %s,arg2: %s" % (arg1,arg2)
   print "arg22" 

def print_two_again(arg1, arg2):
    print "arg1: %s, arg2: %s" %(arg1,arg2)

def print_one(arg1):
    print "arg1: %s" % arg1

def print_none():
    print "no argument"


print_two("Donnie","Tu")
print_two_again("Donnie","Tu")
print_one("Donnie Tu")
print_none()
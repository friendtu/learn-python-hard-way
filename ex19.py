from sys import argv
script,file_name=argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_oneline(currentline, f):
    print "%d : %s" % (currentline, f.readline()),

current_file=open(file_name)

print_all(current_file)
rewind(current_file)

current_line=1
print_oneline(current_line,current_file)

current_line=current_line+1
print_oneline(current_line,current_file)



# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line=line.rstrip()
    print(line.upper())
#inp = fh.read()
#print(inp.upper())

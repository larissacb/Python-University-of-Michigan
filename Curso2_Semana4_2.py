fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
count = 0
fh = open(fname)
for line in fh:
    line=line.rstrip()
    if line.startswith('From '): #verificando se a linha comeca com from
        count=count+1 #incremetando o contador
        fline=line.split() #separando todos as strings da linha
        print(fline[1]) #imprimindo o segundo elemento da linha
print("There were", count, "lines in the file with From as the first word")

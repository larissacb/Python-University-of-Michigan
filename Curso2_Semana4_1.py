fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    wline=line.split() #separando os caracteres de uma linha em uma lista
    for i in range(len(wline)): #percorro toda a lista da linha do arquivo
        string = wline[i]
        if(string not in lst): #vejo se o elemento da lista esta presente em lst. se nao, adiciono
            lst.append(string)
lst.sort() #colocar em ordem
print(lst)

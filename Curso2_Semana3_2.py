# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
soma=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1 #contar o numero de linhas
    line=line.strip()
    dotspos = line.find(':') #encontrando a posição do caractere ':'
    data=line[dotspos+2:26] #separando o numero do resto da string
    num=float(data)#convertendo a stirng para float
    soma=soma+num
media=soma/count
print("Average spam confidence:", media)

